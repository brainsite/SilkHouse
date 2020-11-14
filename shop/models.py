# -*- coding: utf-8 -*-

from django.db import models
from django.templatetags.static import static
from django.conf import settings
from django.db.models import signals

from colors16.models import Colors
from core.utils import my_thumbnail

import os, shutil
from sorl.thumbnail import ImageField

# from django.forms.widgets import Select, SelectMultiple

# TODO Убрать методы с изображениями переписать
# TODO Перенести изображения в модель
# TODO Для каждого типа фото своё поле
# TODO
# TODO

class ScarfManager(models.Manager):
    # def get_queryset(self):
    def all(self):
        return super(ScarfManager, self).get_queryset()

    def update_all(self):
        q = self.all()
        for element in q:
            element.is_multicolor()
            element.save()

    def completed(self):
        q = self.all()
        # Check price
        q = q.filter(price__gt=0)
        # Check weight
        q = q.filter(weight__gt=0)
        # Check colors
        q = q.exclude(l_color__isnull=True)
        q = q.exclude(s_color__isnull=True)
        # Check photo
        q = q.exclude(img__isnull=True)
        return q

    def in_stock(self):
        q = self.completed()
        # В наличии больше одного
        return q.filter(count__gt=0)

    def on_sale(self):
        q = self.in_stock()
        # Не показываем скрытые
        return q.filter(hide__exact=False)

    def on_sale_male(self):
        q = self.on_sale()
        # Строгие цвета
        return q.filter(male__exact=True)

    def on_sale_bicolor(self):
        q = self.on_sale()
        return q.filter(multicolor__exact=False)

    def on_sale_multicolor(self):
        q = self.on_sale()
        return q.filter(multicolor__exact=True)

    def on_sale_lite(self):
        q = self.on_sale()
        # Легче чем 40 или равно
        return q.filter(weight__lte=40)

    def on_sale_hard(self):
        q = self.on_sale()
        # Тяжелее чем 40
        return q.filter(weight__gt=40)

    def sold_out(self):
        q = self.completed()
        # Проданные
        return q.filter(count__lte=0)


class Scarf(models.Model):
    img = ImageField(upload_to='scarfs/', null=True)
    title = models.CharField(u'Название', max_length=128, blank=True)
    count = models.PositiveSmallIntegerField(u'остаток', default=1)
    price = models.PositiveSmallIntegerField(u'цена', default=2000)
    weight = models.PositiveSmallIntegerField(u'Вес', default=25, )
    l_color = models.ForeignKey(Colors, related_name='l_color', null=True, blank=True)
    s_color = models.ManyToManyField(Colors, related_name='s_color', blank=True)
    multicolor = models.BooleanField(u'Цветной', default=False, )
    male = models.BooleanField(u'Строгие тона', default=False, )
    hide = models.BooleanField(u'Скрыть', default=False)
    objects = ScarfManager()

    def __str__(self):
        if self.title:
            return u'Шарф id.{} ({})'.format(self.id, self.title)
        else:
            return u'Шарф id.{}'.format(self.id)

    # Save filename as id.jpg
    # https://groups.google.com/forum/#!topic/django-users/PebyfpMzUyg
    def get_path(self, filename):
        save_name = os.path.join('scarfs', 'silkhouse_id_%s.jpg' % self.id)
        current_path = os.path.join(settings.MEDIA_ROOT, self.img.name)
        new_path = os.path.join(settings.MEDIA_ROOT, save_name)
        print(current_path)
        if os.path.exists(current_path):
            print('yo ho')
        shutil.move(current_path, new_path)
        return save_name

    def save(self):
        # if self.id is None:
        super(Scarf, self).save()
        self.img = self.get_path(self.img)
        super(Scarf, self).save()

    class Meta:
        ordering = ['id']
        verbose_name = u'Платок'
        verbose_name_plural = u'Платки'

    def get_absolute_url(self):
        return "/shop/product/%i/" % self.id


    # Update and signals methods

    def is_multicolor(self):
        if self.s_color.all().count() > 1:
            self.multicolor = True
        else:
            self.multicolor = False

def update_scarf(sender, instance, **kwargs):
    instance.is_multicolor()

signals.post_save.connect(update_scarf, sender=Scarf)

