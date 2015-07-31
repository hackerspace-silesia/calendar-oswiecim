# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0018_category_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(default='panel-primary', max_length=16, choices=[('panel-primary', 'Niebieski'), ('panel-success', 'Zielony'), ('panel-info', 'Jasno niebieski'), ('panel-warning', 'Żółty'), ('panel-danger', 'Czerwony')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='orgs',
            field=models.ManyToManyField(verbose_name='Organizator', related_name='events', blank=True, to='calendars.Organizer'),
        ),
    ]
