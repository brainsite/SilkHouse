# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colors16', '0002_colors_alias'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colors',
            options={'ordering': ['id'], 'verbose_name_plural': 'Цветов', 'verbose_name': 'Цвет'},
        ),
        migrations.AlterField(
            model_name='colors',
            name='alias',
            field=models.CharField(blank=True, max_length=128, verbose_name='Алиас'),
        ),
    ]
