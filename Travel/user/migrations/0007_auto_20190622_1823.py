# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-22 10:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190622_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='uemail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='info',
            old_name='uphone',
            new_name='phone',
        ),
    ]
