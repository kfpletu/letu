# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-22 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190622_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='phone',
            field=models.IntegerField(verbose_name='手机号'),
        ),
    ]