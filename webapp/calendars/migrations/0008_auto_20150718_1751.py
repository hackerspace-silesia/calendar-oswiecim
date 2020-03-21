# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendars', '0007_auto_20150718_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizer',
            name='events',
            field=models.ManyToManyField(to='calendars.Event'),
        ),
        migrations.AddField(
            model_name='organizer',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
        ),
    ]
