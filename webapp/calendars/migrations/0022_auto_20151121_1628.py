# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0021_auto_20151121_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='category',
            new_name='categories',
        ),
    ]
