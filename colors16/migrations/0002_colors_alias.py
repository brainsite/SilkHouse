# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colors16', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colors',
            name='alias',
            field=models.CharField(max_length=128, blank=True, verbose_name='Название'),
        ),
    ]
