# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-26 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=20, verbose_name='酒店名')),
                ('house_count', models.IntegerField(default=30, verbose_name='房间数量')),
                ('order_count', models.IntegerField(default=0, verbose_name='下单次数')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='house',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.House'),
        ),
        migrations.AddField(
            model_name='room',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.House'),
        ),
    ]
