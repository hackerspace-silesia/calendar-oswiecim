# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0010_auto_20150718_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='url',
            field=models.URLField(blank=True, verbose_name='Adres www', null=True),
        ),
    ]
