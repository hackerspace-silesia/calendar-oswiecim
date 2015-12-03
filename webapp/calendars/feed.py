from django_ical.views import ICalFeed
from calendars.models import Event


class EventFeed(ICalFeed):
    product_id = '-//Biblioteka-Oswiecim//Kalendarz//PL'
    timezone = 'UTC'
    file_name = "event.ics"

    def items(self):
        return Event.objects.all().order_by('-start_time')

    def item_guid(self, item):
        return item.pk

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_start_datetime(self, item):
        return item.start_time

    def item_end_datetime(self, item):
        return item.end_time

    def item_link(self, item):
        return item.url or ''