from django.contrib import admin

# Register your models here.
from .models import Event, Organizer, Category


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user', 'start_time', 'end_time')
    search_fields = ['title', 'description']
    fields = ('title', 'place', 'location', 'description', 'categories',
              'start_time', 'end_time', 'image', 'orgs', 'user', 'latitude',
              'longitude')

    class Media:
        css = {
            'screen': ('css/admin.css',)
        }
        js = ('js/vendor/jquery.min.js',)

admin.site.register(Event, EventAdmin)
admin.site.register(Organizer)
admin.site.register(Category)
