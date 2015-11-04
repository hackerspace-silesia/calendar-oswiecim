import datetime

from braces.views import LoginRequiredMixin
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

from .forms import EventForm, LoginForm
from .models import Event, Organizer
from .mixins import HasAccessWithOrganizerMixin, HasAccessMixin


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(start_time__gte=datetime.datetime.now()).order_by('start_time')[:12]
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
    def get(self, request, *args, **kwargs):
        if not self.has_access(request.user)[0]:
            return redirect('/')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.has_access(request.user)[0]:
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


class EventCreateView(EventFieldsMixin, CreateView, HasAccessMixin, HasAccessView):
    action = 'add'

    def post(self, request, *args, **kwargs):
        resp = super().post(request, *args, **kwargs)
        if self.object is not None:
            try:
                org = request.user.organizer
            except Organizer.DoesNotExist:
                pass
            else:
                self.object.orgs.add(org)
            self.object.user = request.user
            self.object.save()
        return resp


class EventUpdateView(EventFieldsMixin, UpdateView, HasAccessWithOrganizerMixin, HasAccessView):
    action = 'change'


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
