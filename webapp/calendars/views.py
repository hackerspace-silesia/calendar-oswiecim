from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Event


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        return context


class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'event.html'
    context_object_name = 'event'