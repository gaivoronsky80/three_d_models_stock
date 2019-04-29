# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-25 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('three_d_models_stock_app', '0002_auto_20190423_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='cover',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='model',
            name='link',
            field=models.FileField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]