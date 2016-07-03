# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_service', '0010_auto_20160702_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentstatus',
            name='payment_status',
        ),
    ]
