# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art_Movement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=200, unique=True)),
                ('movement_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist', to='main.Art_Movement')),
            ],
            managers=[
                ('randoms', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionImage', models.ImageField(upload_to='')),
                ('point', models.IntegerField(blank=True, null=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='main.Artist')),
                ('category', models.ManyToManyField(related_name='category', to='main.Category')),
            ],
        ),
    ]
