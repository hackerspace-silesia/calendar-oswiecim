# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0004_auto_20150718_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True, verbose_name='Koniec wydarzenia', null=True),
        ),
    ]
