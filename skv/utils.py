# -*- coding: utf-8 -*-

"""
from PIL import Image

# 2056 x 3088

img = Image.open('1.JPG')
img.load()

box = (1500, 500, 2100, 900)

img = img.crop(box)

img.thumbnail((300, 200))

img.save('thumbnail.jpeg')
"""

from __future__ import print_function
import os
from PIL import Image

size = (36, 72)

for infile in os.listdir('/home/skv/PycharmProjects/SilkDjango/static/images/laundry/original'):
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for", infile)

######################################################################


class DirImages:

    def __init__(self, path=False, pk=False):
        self.SCARF_IMG_DIR = os.path.join(path, pk)

    def images_uri(self):
        path = os.path.join(settings.STATIC_URL, self.SCARF_IMG_DIR, format(self.id))
        return path

    def images_dir(self):
        path = os.path.join(settings.STATIC_PATH, self.SCARF_IMG_DIR, format(self.id))
        if not os.path.isdir(path):
            os.mkdir(path)
        return path

    def thumbnail_path(self):
        dir = self.images_dir()
        img = os.path.join(dir, 'thumbnail.jpeg')
        if not os.path.isfile(img):
            img = False
        return img

    def thumbnail_uri(self):
        if self.thumbnail_path():
            uri = os.path.join(self.images_uri(), 'thumbnail.jpeg')
        else:
            uri = os.path.join(settings.STATIC_URL, self.SCARF_IMG_DIR, 'no_thumbnail.jpeg')
        return uri

    def images_uris(self):
        uris = []
        imgs = os.listdir(self.images_dir())
        imgs = [f for f in imgs if not f.endswith('thumbnail.jpeg') and not f.startswith('thumbnail.jpeg')]
        for img in imgs:
            uri = os.path.join(self.images_uri(), img)
            uris.append(uri)
        return uris

    class Meta:
        abstract = True
        verbose_name = u'Изображение'
        verbose_name_plural = u'Изображения'

    def images_first(self):
        return self.images_uris()[0]

    #
    # # Админка теги модели
    # def thumbnail_tag(self):
    #     return u'<img src="{}" />'.format(self.thumbnail_uri())
    # thumbnail_tag.short_description = 'thumbnail'
    # thumbnail_tag.allow_tags = True
    #
    # def images_tags(self):
    #     u"""
    #     Возвращаем список <img src=...> или строку.
    #     Необходимо переписать для нормального отображения
    #     Используеться в shop.admin.scarf
    #     """
    #     tags = []
    #     imgs = self.images_uris()
    #     if len(imgs) < 1:
    #         return u'Фотографий нет'
    #     for img in imgs:
    #         tag = u'<img src="{}">'.format(img)
    #         tags.append(tag)
    #     return ' '.join(tags)
    # images_tags.short_description = 'images'
    # images_tags.allow_tags = True
    #
    #
    # def thumbnail_create(self):
    #     """ Тестовый метод """
    #     try:
    #         uri = self.images_uris()[0]
    #     except Exception:
    #         print(Exception)
    #     else:
    #         my_thumbnail(uri)    pass
    #
    #
