# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0012_auto_20150718_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='events',
            new_name='orgs',
        ),
    ]
