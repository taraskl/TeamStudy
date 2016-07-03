# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_service', '0008_auto_20160702_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentstatus',
            name='payment_status',
            field=models.CharField(default=1, max_length=1, choices=[('Y', 'Yes'), ('N', 'No'), ('E', 'Erorr')]),
            preserve_default=False,
        ),
    ]
