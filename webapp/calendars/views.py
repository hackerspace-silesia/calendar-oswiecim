from django.shortcuts import render, redirect

from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

from .models import Event
from .forms import LoginForm

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
