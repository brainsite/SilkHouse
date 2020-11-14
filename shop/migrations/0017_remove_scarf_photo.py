# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20150625_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scarf',
            name='photo',
        ),
    ]
