from django.contrib import admin

# Register your models here.
from calendars.models import Event, Organizer

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_time', 'end_time')

admin.site.register(Event, EventAdmin)
admin.site.register(Organizer)