# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendars', '0025_auto_20160222_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizer',
            name='user',
        ),
        migrations.AddField(
            model_name='organizer',
            name='user',
            field=models.ManyToManyField(verbose_name='Użytkownik', related_name='organizer', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
