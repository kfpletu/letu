# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-26 04:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0006_auto_20190626_0833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scenic1',
            options={'verbose_name': '景点信息表', 'verbose_name_plural': '景点信息表'},
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='play_time',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='sumprice',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_num',
        ),
    ]
