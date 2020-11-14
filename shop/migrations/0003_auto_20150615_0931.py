# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colors16', '0003_auto_20150615_0931'),
        ('shop', '0002_auto_20150615_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scarf',
            name='l_side',
        ),
        migrations.RemoveField(
            model_name='scarf',
            name='s_side',
        ),
        migrations.AddField(
            model_name='scarf',
            name='l_color',
            field=models.ForeignKey(null=True, related_name='l_color', blank=True, to='colors16.Colors'),
        ),
    ]
