# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-25 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenic1',
            name='open_time',
            field=models.CharField(max_length=65, verbose_name='开放时间'),
        ),
    ]
