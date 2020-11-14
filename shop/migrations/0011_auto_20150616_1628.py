# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_scarf_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scarf',
            name='show',
        ),
        migrations.AddField(
            model_name='scarf',
            name='hide',
            field=models.BooleanField(default=False, verbose_name='Скрыто'),
        ),
    ]
