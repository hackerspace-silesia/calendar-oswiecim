# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0026_auto_20160222_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizer',
            name='url',
            field=models.URLField(null=True, blank=True, verbose_name='Adres www'),
        ),
    ]
