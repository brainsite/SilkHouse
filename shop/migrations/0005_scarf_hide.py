# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_scarf_s_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='scarf',
            name='hide',
            field=models.BooleanField(verbose_name='Скрыть', default=False),
        ),
    ]
