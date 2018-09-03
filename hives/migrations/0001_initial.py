# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HiveModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfHive', models.IntegerField(unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('additional_info', models.CharField(max_length=500)),
            ],
        ),
    ]