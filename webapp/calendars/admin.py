from django.contrib.gis import admin

# Register your models here.
from calendars.models import Event, Organizer

class EventAdmin(admin.OSMGeoAdmin):
    list_display = ('title', 'description', 'start_time', 'end_time')

admin.site.register(Event, EventAdmin)
admin.site.register(Organizer)