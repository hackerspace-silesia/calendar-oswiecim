from django.contrib.gis import forms
from django.contrib.admin import widgets
from .models import Event


class LoginForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika');
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput())


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = (
            'title', 'description',
            'category', 'start_time',
            'end_time', 'image', 'place',
        )
        widgets = {
            'start_time': widgets.AdminSplitDateTime,
            'end_time': widgets.AdminSplitDateTime
        }
