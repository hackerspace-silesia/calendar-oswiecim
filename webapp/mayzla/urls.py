"""mayzla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.urls import re_path, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from calendars.views import HomeView, EventDetailView, EventListView, events_api
from calendars.views import EventCreateView, EventUpdateView
from calendars.views import LoginView, logout_view
from calendars.feed import EventFeed

urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name="index"),
    re_path(r'^wydarzenie/json/$', events_api, name="event_json_list"),
    re_path(r'^wydarzenie/$', EventListView.as_view(), name="event_list"),
    re_path(r'^wydarzenie/(?P<pk>\d+)/$', EventDetailView.as_view(), name="event_details"),
    re_path(r'^wydarzenie/dodaj/$', EventCreateView.as_view(), name="event_create"),
    re_path(r'^wydarzenie/(?P<pk>\d+)/edycja/$', EventUpdateView.as_view(), name="event_update"),
    #url(r'^wydarzenie/(?P<pk>\d+)/usun/$', EventDeleteView.as_view(), name="event_details"),
    re_path(r'^onas/$', TemplateView.as_view(template_name="about_us.html"), name="about_us"),
    re_path(r'^zaloguj/$', LoginView.as_view(), name="login"),
    re_path(r'^wyloguj/$', logout_view, name="logout"),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^event.ics$', EventFeed(), name='ical'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)

