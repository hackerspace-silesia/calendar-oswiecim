# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0002_organizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='event/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo/%m/'),
        ),
    ]
