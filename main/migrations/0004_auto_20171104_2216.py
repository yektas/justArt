# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0003_auto_20171028_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ManyToManyField(related_name='category', to='main.Category'),
        ),
    ]