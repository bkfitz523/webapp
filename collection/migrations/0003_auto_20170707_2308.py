# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-07 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20170707_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type_2',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
