import json
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from pip._vendor.html5lib import serializer

from functools import wraps

from .models import Event
from .forms import LoginForm, EventForm



class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        return context


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)

        @login_required
        @wraps(view)
        def inner_view(request, *args, **kwargs):
            try:
                _ = request.user.organizer
            except ObjectDoesNotExist:
                return redirect('/')
            return view(request, *args, **kwargs)
        return inner_view


class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    template_name = 'event.html'
    context_object_name = 'event'


class EventFieldsMixin(LoginRequiredMixin):
    model = Event
    form_class = EventForm
    template_name = 'event_edit.html'
    context_object_name = 'event'
    success_url = '/'


class EventCreateView(EventFieldsMixin, CreateView):
    def post(self, request, *args, **kwargs):
        resp = super().post(request, *args, **kwargs)
        if self.object is not None:
            org = request.user.organizer
            self.object.orgs.add(org)
        return resp


class EventUpdateView(EventFieldsMixin, UpdateView):
    def get(self, request, *args, **kwargs):
        if not self.has_access(request.user):
            return redirect('/')
        return super().get(request, *args, **kwargs)

    def has_access(self, user):
        obj = self.get_object()
        return obj.orgs.filter(pk=user.organizer.pk).exists()

    def post(self, request, *args, **kwargs):
        if not self.has_access(request.user):
            return redirect('/')
        return super().post(request, *args, **kwargs)


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
        events = Event.objects.filter(Q(start_time__year=year,
                             start_time__month=month)|
                             Q(start_time__year=year,
                             start_time__month=month))
        return HttpResponse(serializers.serialize('json', events, fields=('title','description', 'start_time', 'end_time')), content_type="application/json")
    else:
        return HttpResponse(status=400, content_type='text/html')

