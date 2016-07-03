# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_service', '0007_clientorders'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, null=True, blank=True)),
                ('payment_status', models.CharField(blank=True, max_length=1, null=True, choices=[('Y', 'Yes'), ('N', 'No'), ('E', 'Erorr')])),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='dataOrder',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='client',
        ),
        migrations.AddField(
            model_name='order',
            name='add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='all_payments',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='edit',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='order_amount',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='prise',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
