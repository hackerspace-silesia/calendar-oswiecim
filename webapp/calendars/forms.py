from django import forms
from django.contrib.admin import widgets
from datetimewidget.widgets import DateTimeWidget
from .models import Event


class LoginForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput())


data_time_options = {
    'format': 'dd-mm-yyyy HH:ii'
}

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = (
            'title', 'description',
            'category', 'start_time',
            'end_time', 'image', 'place',
        )
        widgets = {
            'start_time': DateTimeWidget(bootstrap_version=3, usel10n=True, options=data_time_options),
            'end_time': DateTimeWidget(bootstrap_version=3, usel10n=True, options=data_time_options),
        }
