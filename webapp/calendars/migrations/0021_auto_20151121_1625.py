# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0020_auto_20151104_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='category',
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ManyToManyField(null=True, to='calendars.Category', blank=True, verbose_name='Kategoria'),
        ),
    ]
