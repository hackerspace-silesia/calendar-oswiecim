# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendars', '0019_auto_20150731_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='point',
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(verbose_name='Użytkownik', to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(verbose_name='Kategoria', null=True, blank=True, to='calendars.Category'),
        ),
    ]
