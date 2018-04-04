# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_participante_inscripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'SOCIO'), (2, 'DAMA ROTARIA'), (3, 'ROTARACT'), (4, 'SOCIOCON')], default=1),
        ),
    ]
