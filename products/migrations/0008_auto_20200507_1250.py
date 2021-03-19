# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-07 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200507_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('2000 x 1920', '2000 x 1920'), ('1080 x 1920', '1080 x 1920'), ('720 x 720', '720 x 720'), ('720 x 400', '720 x 400'), ('400 x 400', '400 x 400'), ('200 x 200', '200 x 200'), ('100 x 100', '100 x 100')], default='1080 x 1920', max_length=15),
        ),
    ]