from django.core.management.base import BaseCommand
from ...models import Event

from json import load as load_json

import sys
import datetime


formats = [
    '%d.%m.%Y @ %H:%M',
    '%H:%M',
    '%d.%m.%Y',
    '%d.%m.%Y @ Całodniowe',
]


class Command(BaseCommand):
    help = 'Load events from scrapper'

    @staticmethod
    def add_arguments(parser):
        parser.add_argument('files_path', type=str)

    def handle(self, *args, **options):
        dir_path = options['files_path']

        with open(dir_path) as fp:
            all_data = load_json(fp)

        for i, data in enumerate(all_data):
            self.load_event(data)
            if i % 10 == 0:
                sys.stdout.write('.')
                sys.stdout.flush()
        sys.stdout.write('\nDone\n')

    @classmethod
    def load_event(cls, data):
        raw_dt = data['data / godzina']
        dts = [cls.get_dt(r.strip()) for r in raw_dt.split('-')]

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

        try:
            Event.objects.get_or_create(
                title=data['tytuł'],
                place=data.get('miejsce') or '',
                description=data.get('opis') or '',
                start_time=dts[0],
                end_time=dts[1] if len(dts) > 1 else None,
            )
        except Event.MultipleObjectsReturned:
            pass

    @staticmethod
    def get_dt(raw_dt):
        for format in formats:
            try:
                return datetime.datetime.strptime(raw_dt, format)
            except ValueError:
                continue
        raise ValueError(repr(raw_dt))