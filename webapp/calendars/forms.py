from django import forms
from django.contrib.admin import widgets
from .models import Event


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            'title', 'description',
            'start_time', 'end_time',
            'image', 'place', 'point'
        )
        widgets = {
            'start_time': widgets.AdminSplitDateTime,
            'end_time': widgets.AdminSplitDateTime
        }
