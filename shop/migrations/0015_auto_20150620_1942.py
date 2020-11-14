# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_scarf_male'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scarf',
            old_name='multicolors',
            new_name='multicolor',
        ),
    ]
