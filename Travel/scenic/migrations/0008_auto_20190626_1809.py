# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-26 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0007_auto_20190626_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenic1',
            name='sce_name',
            field=models.CharField(max_length=8, unique=True, verbose_name='景点名称'),
        ),
    ]
