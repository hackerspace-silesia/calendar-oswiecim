# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0017_auto_20150731_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.CharField(choices=[('Niebieski', 'panel-primary'), ('Zielony', 'panel-success'), ('Jasno niebieski', 'panel-info'), ('Żółty', 'panel-warning'), ('Czerwony', 'panel-danger')], max_length=16, default='panel-primary'),
        ),
    ]
