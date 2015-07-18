# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from json import load as load_json
from os import path
from functools import wraps
from datetime import datetime

DIR = path.dirname(path.abspath(__file__))
FIXTURE_DIR = path.join(DIR, '..', 'fixtures')


def load_data(cls_name, fixture):

    def outer_func(func):

        @wraps(func)
        def inner_func(apps, schema_editor):
            cls = apps.get_model("calendars", cls_name)

            with open(path.join(FIXTURE_DIR, fixture)) as fp:
                for data in load_json(fp):
                    func(cls, data)

        def reverse_func(apps, schema_editor):
            cls = apps.get_model("calendars", cls_name)
            cls.objects.all().delete()

        return migrations.RunPython(inner_func, reverse_func)
    return outer_func


formats = [
    '%d.%m.%Y @ %H:%M',
    '%H:%M',
    '%d.%m.%Y',
    '%d.%m.%Y @ Całodniowe',
]


def get_dt(raw_dt):
    for format in formats:
        try:
            return datetime.strptime(raw_dt, format)
        except ValueError:
            continue
    raise ValueError(repr(raw_dt))


@load_data('Event', 'data.json')
def load_events(cls, data):
    raw_dt = data['data / godzina']
    dts = [get_dt(r.strip()) for r in raw_dt.split('-')]

    if len(dts) > 1:
        start_dt, end_dt = dts[0:2]
        if end_dt.year == 1900:
            dts[1] = end_dt.replace(
                start_dt.year,
                start_dt.month,
                start_dt.day
            )
    else:
        dts.append(dts[0])

    print(data['old_eid'])
    cls.objects.create(
        title=data['tytuł'],
        place=data.get('miejsce') or '',
        description=data.get('opis') or '',
        start_time=dts[0],
        end_time=dts[1] if len(dts) > 1 else None,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0010_auto_20150718_2023'),
    ]

    operations = [
        load_events,
    ]
