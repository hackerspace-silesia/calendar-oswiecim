# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0007_auto_20150718_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
