from django.contrib import admin

# Register your models here.
from calendars.models import Event, Organizer

admin.site.register(Event)
admin.site.register(Organizer)