# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0006_event_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.CharField(default=datetime.datetime(2015, 7, 18, 16, 29, 46, 206995), max_length=120, verbose_name='Miejsce'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, blank=True, verbose_name='Miejsce na mapie', null=True),
        ),
    ]
