# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20170718_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productImage',
            field=models.ImageField(blank=True, upload_to='products', verbose_name='Product Image'),
        ),
    ]
