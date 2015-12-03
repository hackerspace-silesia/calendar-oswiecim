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
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from calendars.views import HomeView, EventDetailView, EventListView, events_api
from calendars.views import EventCreateView, EventUpdateView
from calendars.views import LoginView, logout_view
from calendars.feed import EventFeed

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="index"),
    url(r'^wydarzenie/json/$', events_api, name="event_json_list"),
    url(r'^wydarzenie/$', EventListView.as_view(), name="event_list"),
    url(r'^wydarzenie/(?P<pk>\d+)/$', EventDetailView.as_view(), name="event_details"),
    url(r'^wydarzenie/dodaj/$', EventCreateView.as_view(), name="event_create"),
    url(r'^wydarzenie/(?P<pk>\d+)/edycja/$', EventUpdateView.as_view(), name="event_update"),
    #url(r'^wydarzenie/(?P<pk>\d+)/usun/$', EventDeleteView.as_view(), name="event_details"),
    url(r'^onas/$', TemplateView.as_view(template_name="about_us.html"), name="about_us"),
    url(r'^zaloguj/$', LoginView.as_view(), name="login"),
    url(r'^wyloguj/$', logout_view, name="logout"),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^event.ics$', EventFeed(), name='ical'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT})]