# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20150620_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='scarf',
            name='male',
            field=models.BooleanField(default=False, verbose_name='Строгие тона'),
        ),
    ]
