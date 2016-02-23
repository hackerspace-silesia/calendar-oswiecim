from django.contrib import admin
from easy_select2 import select2_modelform

# Register your models here.
from .models import Event, Organizer, Category


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user', 'start_time', 'end_time')
    search_fields = ['title', 'description']
    fields = ('title', 'place', 'location', 'description', 'categories',
              'start_time', 'end_time', 'image', 'orgs', 'user', 'latitude',
              'longitude')

    form = select2_modelform(Event)

    class Media:
        css = {
            'screen': ('css/admin.css',)
        }
        js = ('js/vendor/jquery.min.js',)

class OrganizerAdmin(admin.ModelAdmin):
    form = select2_modelform(Organizer, attrs={'width': '400px'})

admin.site.register(Event, EventAdmin)
admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(Category)
