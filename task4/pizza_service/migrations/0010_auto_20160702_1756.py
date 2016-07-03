# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_service', '0009_auto_20160702_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='add',
            field=models.DateTimeField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='edit',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 2, 17, 56, 23, 848475, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
