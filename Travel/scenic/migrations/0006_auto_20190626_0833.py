# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-26 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0005_auto_20190626_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenic1',
            name='open_time',
            field=models.CharField(max_length=200, verbose_name='开放时间'),
        ),
    ]