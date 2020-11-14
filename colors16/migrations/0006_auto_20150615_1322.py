# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colors16', '0005_auto_20150615_1117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colors',
            options={'verbose_name': 'Цвет', 'ordering': ['title'], 'verbose_name_plural': 'Цветов'},
        ),
    ]
