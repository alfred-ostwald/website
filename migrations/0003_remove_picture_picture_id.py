# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 21:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20171128_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='picture_id',
        ),
    ]
