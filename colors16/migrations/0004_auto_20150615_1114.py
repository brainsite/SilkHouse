# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colors16', '0003_auto_20150615_0931'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colors',
            options={'verbose_name_plural': 'Цветов', 'default_permissions': (), 'verbose_name': 'Цвет', 'ordering': ['title']},
        ),
    ]
