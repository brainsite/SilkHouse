# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colors16', '0004_auto_20150615_1114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colors',
            options={'ordering': ['title'], 'verbose_name_plural': 'Цветов', 'verbose_name': 'Цвет', 'permissions': (('can_change_colors16', 'can_change_colors16'),)},
        ),
    ]
