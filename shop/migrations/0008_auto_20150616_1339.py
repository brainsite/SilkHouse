# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20150615_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scarf',
            name='show',
            field=models.BooleanField(default=True, verbose_name='В магазине'),
        ),
        migrations.AlterField(
            model_name='scarf',
            name='weight',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Вес'),
        ),
    ]
