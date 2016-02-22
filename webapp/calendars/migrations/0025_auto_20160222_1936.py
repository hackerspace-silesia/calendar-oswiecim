# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import osm_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0024_auto_20160220_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='categories',
            field=models.ManyToManyField(to='calendars.Category', blank=True, verbose_name='Kategoria'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=osm_field.fields.OSMField(lat_field='latitude', lon_field='longitude', default='Oświęcim', verbose_name='Położenie na mapie'),
        ),
    ]
