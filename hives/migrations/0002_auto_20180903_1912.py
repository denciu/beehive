# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-03 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hivemodel',
            name='additional_info',
            field=models.CharField(blank=True, default='', max_length=500),
            preserve_default=False,
        ),
    ]