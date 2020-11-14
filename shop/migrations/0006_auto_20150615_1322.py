# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_scarf_hide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scarf',
            name='hide',
        ),
        migrations.AddField(
            model_name='scarf',
            name='available',
            field=models.BooleanField(verbose_name='Открыт для просмотра', default=True),
        ),
    ]
