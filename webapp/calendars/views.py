import datetime

from braces.views import LoginRequiredMixin
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.contrib import messages
from django.utils import timezone
from itertools import chain

from .forms import EventForm, LoginForm
from .models import Event, Organizer
from .mixins import HasAccessWithOrganizerMixin, HasAccessMixin


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        future_events = Event.objects.filter(start_time__gte=datetime.datetime.now()).order_by('start_time')[:settings.EVENTS_NUMBER_HOMEPAGE]
        past_events = Event.objects.filter(start_time__lt=datetime.datetime.now()).order_by('-start_time')[:settings.EVENTS_NUMBER_HOMEPAGE - future_events.count()]
        dt_now = timezone.now()
        for event in past_events:
            event.is_old = event.end_time < dt_now
        context['events'] = list(chain(future_events, past_events))
        return context


class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['events_as_json'] = serializers.serialize(
            'json', self.object_list,
            fields=('title', 'description', 'start_time', 'end_time'))
        return context


class HasAccessView(object):
    HAS_ACCESS_ERROR_MSG = 'Nie masz uprawnień do tej strony!'

    def get(self, request, *args, **kwargs):
        if not self.has_access(request.user)[0]:
            messages.error(self.HAS_ACCESS_ERROR_MSG)
            return redirect('/')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.has_access(request.user)[0]:
            messages.error(self.HAS_ACCESS_ERROR_MSG)
            return redirect('/')
        return super().post(request, *args, **kwargs)


class EventDetailView(DetailView, HasAccessWithOrganizerMixin):
    model = Event
    template_name = 'event.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_edit'] = self.has_access(self.request.user, 'change')[0]
        return context


class EventFieldsMixin(LoginRequiredMixin):
    model = Event
    form_class = EventForm
    template_name = 'event_edit.html'
    context_object_name = 'event'
    success_url = '/'


class EventCreateView(EventFieldsMixin, HasAccessView, CreateView, HasAccessMixin):
    action = 'add'

    def post(self, request, *args, **kwargs):
        resp = super().post(request, *args, **kwargs)
        if not self.has_access(request.user)[0]:
            return resp
        if self.object is not None:
            try:
                org = Organizer.objects.get(user=request.user.id)
            except Organizer.DoesNotExist:
                pass
            else:
                self.object.orgs.add(org)
            self.object.user = request.user
            self.object.save()
        return resp

    def form_valid(self, form):
        msg = "Pomyślnie dodano wydarzenie %s" % form.data['title']
        messages.success(self.request, msg)
        return super().form_valid(form)


class EventUpdateView(EventFieldsMixin, HasAccessView, UpdateView, HasAccessWithOrganizerMixin):
    action = 'change'

    def form_valid(self, form):
        msg = "Pomyślnie zaaktulizowano wydarzenie %s" % form.data['title']
        messages.success(self.request, msg)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if self.login(request, form):
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def login(self, request, form):
        if not form.is_valid():
            return False

        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        if user is None:
            messages.error(
                request,
                'Hasło oraz/lub nazwa użytkownika jest niepoprawna'
            )
            return False

        if not user.is_active:
            messages.error(request, 'Użytkownik nie jest aktywny')
            return False

        login(request, user)
        messages.success(request, 'Zalogowano')
        return True


def logout_view(request):
    logout(request)
    messages.success(request, 'Wylogowano')
    return redirect('/')


def events_api(request):
    month = request.GET.get('month', None)
    year = request.GET.get('year', None)

    if year and month:
        events = Event.objects.filter(
            Q(start_time__year=year, start_time__month=month) |
            Q(start_time__year=year, start_time__month=month))
        return HttpResponse(
            serializers.serialize(
                'json', events,
                fields=('title', 'description', 'start_time', 'end_time')),
            content_type="application/json")
    else:
        return HttpResponse(status=400, content_type='text/html')
