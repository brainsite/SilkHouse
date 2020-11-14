# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20150616_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='scarf',
            name='multicolor',
            field=models.BooleanField(default=False, verbose_name='Цветной'),
        ),
        migrations.AddField(
            model_name='scarf',
            name='photo',
            field=models.BooleanField(default=False, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='scarf',
            name='hide',
            field=models.BooleanField(default=False, verbose_name='Скрыть'),
        ),
    ]
