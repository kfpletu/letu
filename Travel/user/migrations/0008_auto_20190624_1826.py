# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-24 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20190622_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='phone',
            field=models.CharField(max_length=11, unique=True, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='info',
            name='uname',
            field=models.CharField(max_length=15, unique=True, verbose_name='用户姓名'),
        ),
    ]