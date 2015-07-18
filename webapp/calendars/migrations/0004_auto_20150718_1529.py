# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0003_auto_20150718_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(verbose_name='Koniec wydarzenia'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, blank=True, verbose_name='Plakat', upload_to='event/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(verbose_name='Start wydarzenia'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Tytuł'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='logo',
            field=models.ImageField(null=True, blank=True, verbose_name='Logo', upload_to='logo/%m/'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nazwa'),
        ),
    ]
