# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20150615_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scarf',
            old_name='available',
            new_name='show',
        ),
    ]
