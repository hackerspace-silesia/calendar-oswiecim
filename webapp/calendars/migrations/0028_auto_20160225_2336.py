# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0027_organizer_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 25, 22, 36, 34, 720210, tzinfo=utc), verbose_name='Koniec wydarzenia', db_index=True),
            preserve_default=False,
        ),
    ]
