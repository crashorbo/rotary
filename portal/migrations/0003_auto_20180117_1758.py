# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-17 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20180117_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]