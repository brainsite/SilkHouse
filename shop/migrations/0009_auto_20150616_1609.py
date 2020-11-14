# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20150616_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='scarf',
            name='photo',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='scarf',
            name='s_color',
            field=models.ManyToManyField(to='colors16.Colors', related_name='s_color', blank=True),
        ),
    ]
