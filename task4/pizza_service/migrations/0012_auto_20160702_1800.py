# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_service', '0011_remove_paymentstatus_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientorders',
            name='order_ptr',
        ),
        migrations.RemoveField(
            model_name='order',
            name='client',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pizza',
        ),
        migrations.DeleteModel(
            name='PaymentStatus',
        ),
        migrations.DeleteModel(
            name='ClientOrders',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
