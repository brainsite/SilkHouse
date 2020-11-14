# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(verbose_name='Название', max_length=128)),
                ('translate', models.CharField(verbose_name='Цвет', max_length=128)),
                ('code', models.CharField(verbose_name='Hex code', max_length=8)),
            ],
            options={
                'verbose_name': 'Тон',
                'ordering': ['id'],
                'verbose_name_plural': 'Тона',
            },
        ),
    ]
