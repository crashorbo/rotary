# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0016_auto_20180509_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='participante',
            name='credencial',
            field=models.BooleanField(default=False),
        ),
    ]
