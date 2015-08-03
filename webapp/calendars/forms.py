from django.contrib.gis import forms
from django.contrib.admin import widgets
from .models import Event


class LoginForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika');
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput())


class EventForm(forms.ModelForm):
    point = forms.PointField(widget=forms.OSMWidget(),label="Miejsce na mapie")

    class Meta:
        model = Event
        fields = (
            'title', 'description',
            'category', 'start_time',
            'end_time', 'image', 'place', 'point',
        )
        widgets = {
            'start_time': widgets.AdminSplitDateTime,
            'end_time': widgets.AdminSplitDateTime
        }
