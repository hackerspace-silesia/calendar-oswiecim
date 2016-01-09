# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0022_auto_20151121_1628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(max_length=16, default='primary', choices=[('primary', 'Niebieski'), ('success', 'Zielony'), ('info', 'Jasno niebieski'), ('warning', 'Żółty'), ('danger', 'Czerwony')]),
        ),
    ]
