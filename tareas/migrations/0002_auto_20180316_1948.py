# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='duracion_estimada',
            new_name='duracion',
        ),
        migrations.AlterField(
            model_name='tarea',
            name='tiempo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
