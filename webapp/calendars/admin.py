from django.contrib import admin

# Register your models here.
from .models import Event, Organizer, Category


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user', 'start_time', 'end_time')
    search_fields = ['title', 'description']

admin.site.register(Event, EventAdmin)
admin.site.register(Organizer)
admin.site.register(Category)
