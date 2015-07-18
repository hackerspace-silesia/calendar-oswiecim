import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.
from .models import Event


class CalendarViewsTests(TestCase):
    def test_showing_events(self):
        Event.objects.create(title="First Event", description="This is first Event!",
                             start_time=datetime.datetime.now(),
                             end_time=datetime.datetime.now() + datetime.timedelta(hours=5))
        url = reverse('index')
        response = self.client.get(url)
        self.assertContains(response, "First Event")

    def test_showing_details(self):
        event = Event.objects.create(title="Second Event", description="This is second Event!",
                             start_time=datetime.datetime.now(),
                             end_time=datetime.datetime.now() + datetime.timedelta(hours=5))

        url = reverse('event_details', kwargs={'pk':event.id})
        response = self.client.get(url)
        self.assertContains(response, "Second Event")
