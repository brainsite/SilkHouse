# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scarf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name='название акции')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='остаток')),
                ('price', models.PositiveSmallIntegerField(default=0, verbose_name='цена')),
                ('l_side', models.PositiveSmallIntegerField(default=0, choices=[[0, 'Не задан'], [1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, '']], verbose_name='Основной цвет')),
                ('s_side', models.PositiveSmallIntegerField(default=0, choices=[[0, 'Не задан'], [1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, '']], verbose_name='Дополнительный цвет')),
                ('weight', models.PositiveSmallIntegerField(default=0, verbose_name='Вес в граммах')),
            ],
            options={
                'verbose_name_plural': 'Платки',
                'ordering': ['id'],
                'verbose_name': 'Платок',
            },
            bases=(models.Model,),
        ),
    ]
