# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20150620_1901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scarf',
            old_name='multicolor',
            new_name='multicolors',
        ),
    ]
