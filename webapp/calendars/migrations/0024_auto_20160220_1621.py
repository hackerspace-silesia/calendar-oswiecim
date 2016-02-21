# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import osm_field.fields
import osm_field.validators


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0023_auto_20160109_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='latitude',
            field=osm_field.fields.LatitudeField(verbose_name='Długość geograficzna', validators=[osm_field.validators.validate_latitude], default=50.038),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=osm_field.fields.OSMField(verbose_name='Położenie na mapie', null=True, lon_field='longitude', lat_field='latitude'),
        ),
        migrations.AddField(
            model_name='event',
            name='longitude',
            field=osm_field.fields.LongitudeField(verbose_name='Szerokość geograficzna', validators=[osm_field.validators.validate_longitude], default=19.221),
        ),
    ]
