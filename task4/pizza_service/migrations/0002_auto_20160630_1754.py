# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='client',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pizza_service.Client'),
        ),
    ]