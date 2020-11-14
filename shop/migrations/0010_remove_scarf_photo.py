# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20150616_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scarf',
            name='photo',
        ),
    ]
