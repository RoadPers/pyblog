# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-31 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(),
        ),
    ]
