# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_menu_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='prix',
            field=models.FloatField(max_length=255),
        ),
    ]
