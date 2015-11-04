from django.contrib.gis import admin

# Register your models here.
from .models import Event, Organizer, Category

class EventAdmin(admin.OSMGeoAdmin):
    list_display = ('title', 'description', 'user', 'start_time', 'end_time')

admin.site.register(Event, EventAdmin)
admin.site.register(Organizer)
admin.site.register(Category)