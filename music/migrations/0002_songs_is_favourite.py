# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-12 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]
