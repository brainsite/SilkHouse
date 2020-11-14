# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colors16', '0003_auto_20150615_0931'),
        ('shop', '0003_auto_20150615_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='scarf',
            name='s_color',
            field=models.ManyToManyField(blank=True, to='colors16.Colors', related_name='s_color', null=True),
        ),
    ]
