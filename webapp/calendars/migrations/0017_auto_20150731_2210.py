# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0016_auto_20150722_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Opis wydarzenia'),
        ),
        migrations.AlterField(
            model_name='event',
            name='orgs',
            field=models.ManyToManyField(related_name='events', to='calendars.Organizer', verbose_name='Organizator'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='user',
            field=models.OneToOneField(null=True, related_name='organizer', blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(null=True, blank=True, to='calendars.Category', on_delete=models.CASCADE),
        ),
    ]
