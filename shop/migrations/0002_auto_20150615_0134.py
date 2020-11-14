# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scarf',
            name='l_side',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Основной цвет', choices=[[0, 'Не задан'], [1, 'aqua'], [2, 'black'], [3, 'blue'], [4, 'fuchsia'], [5, 'green'], [6, 'gray'], [7, 'lime'], [8, 'maroon'], [9, 'navy'], [10, 'olive'], [11, 'purple'], [12, 'red'], [13, 'silver'], [14, 'teal'], [15, 'white'], [16, 'yellow']]),
        ),
        migrations.AlterField(
            model_name='scarf',
            name='s_side',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Дополнительный цвет', choices=[[0, 'Не задан'], [1, 'aqua'], [2, 'black'], [3, 'blue'], [4, 'fuchsia'], [5, 'green'], [6, 'gray'], [7, 'lime'], [8, 'maroon'], [9, 'navy'], [10, 'olive'], [11, 'purple'], [12, 'red'], [13, 'silver'], [14, 'teal'], [15, 'white'], [16, 'yellow']]),
        ),
        migrations.AlterField(
            model_name='scarf',
            name='title',
            field=models.CharField(blank=True, verbose_name='Название', max_length=128),
        ),
    ]
