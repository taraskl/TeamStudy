# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pizza_service', '0013_auto_20160702_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(blank=True, max_length=256)),
                ('phone', models.CharField(blank=True, max_length=256)),
                ('address', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add', models.DateTimeField()),
                ('edit', models.DateTimeField()),
                ('order_amount', models.IntegerField(blank=True, null=True)),
                ('all_payments', models.IntegerField(blank=True, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('payment_status', models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('E', 'Erorr')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('prise', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClientOrders',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pizza_service.Order')),
            ],
            bases=('pizza_service.order',),
        ),
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza_service.Client'),
        ),
        migrations.AddField(
            model_name='order',
            name='pizza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pizza_service.Pizza'),
        ),
    ]
