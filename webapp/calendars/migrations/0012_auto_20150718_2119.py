# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0011_event_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizer',
            name='events',
        ),
        migrations.AddField(
            model_name='event',
            name='events',
            field=models.ManyToManyField(to='calendars.Organizer', related_name='events'),
        ),
    ]
