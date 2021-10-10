# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0009_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizer',
            name='events',
            field=models.ManyToManyField(related_name='orgs', to='calendars.Event'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='user',
            field=models.OneToOneField(related_name='organizer', null=True, to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
        ),
    ]
