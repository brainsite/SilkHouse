# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20150620_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='scarf',
            name='img',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='scarfs/'),
        ),
        migrations.AlterField(
            model_name='scarf',
            name='count',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='остаток'),
        ),
        migrations.AlterField(
            model_name='scarf',
            name='price',
            field=models.PositiveSmallIntegerField(default=2000, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='scarf',
            name='weight',
            field=models.PositiveSmallIntegerField(default=25, verbose_name='Вес'),
        ),
    ]
