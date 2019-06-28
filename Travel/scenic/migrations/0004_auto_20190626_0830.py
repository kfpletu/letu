# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-26 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0003_auto_20190626_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenic1',
            name='brief_des',
            field=models.CharField(max_length=40, verbose_name='景点简述'),
        ),
        migrations.AlterField(
            model_name='scenic1',
            name='bus_go',
            field=models.CharField(max_length=40, verbose_name='公交'),
        ),
        migrations.AlterField(
            model_name='scenic1',
            name='car_go',
            field=models.CharField(max_length=40, verbose_name='自驾'),
        ),
    ]