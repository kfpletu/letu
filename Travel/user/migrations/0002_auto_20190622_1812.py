# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-22 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='phone',
            field=models.IntegerField(max_length=11, verbose_name='手机号'),
        ),
    ]
