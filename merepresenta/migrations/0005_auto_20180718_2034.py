# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-18 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merepresenta', '0004_coaligacao_partido'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='race',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='coaligacao',
            name='mark',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='partido',
            name='mark',
            field=models.IntegerField(null=True),
        ),
    ]
