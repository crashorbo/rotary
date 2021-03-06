# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-29 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0012_auto_20180327_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default=(2, 'DAMA ROTARIA'), max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('monto', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('estado', models.BooleanField(default=False)),
                ('detalle_deposito', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='participante',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='participante',
            name='detalle_deposito',
        ),
        migrations.RemoveField(
            model_name='participante',
            name='email',
        ),
        migrations.RemoveField(
            model_name='participante',
            name='monto',
        ),
    ]
