from django import forms
from django.contrib.admin import widgets
from datetimewidget.widgets import DateTimeWidget
from .models import Event


class LoginForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput())


date_time_options = {
    'format': 'dd.mm.yyyy hh:ii',
    'language': 'pl'
}

def dt_widget():
    return DateTimeWidget(
        bootstrap_version=3,
        options=date_time_options
    )


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = (
            'title', 'place',
            'description', 'categories',
            'start_time', 'end_time',
            'image', 'url',
        )
        widgets = {
            'start_time': dt_widget(),
            'end_time': dt_widget(),
        }
