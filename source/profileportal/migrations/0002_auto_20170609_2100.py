# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileportal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsite',
            name='codechef',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='studentsite',
            name='github',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='studentsite',
            name='hackerearth',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='studentsite',
            name='spoj',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]