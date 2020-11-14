# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colors16', '0006_auto_20150615_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colors',
            options={'ordering': ['title'], 'verbose_name_plural': 'Цвета', 'verbose_name': 'Цвет'},
        ),
    ]
