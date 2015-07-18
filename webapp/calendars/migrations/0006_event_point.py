# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0005_auto_20150718_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Miejsce na mapie'),
        ),
    ]
