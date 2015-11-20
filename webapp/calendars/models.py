from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin import widgets


class Event(models.Model):
    start_time = models.DateTimeField(db_index=True, verbose_name="Start wydarzenia")
    end_time = models.DateTimeField(db_index=True, blank=True, null=True, verbose_name="Koniec wydarzenia")
    title = models.CharField(max_length=120, verbose_name="Tytuł")
    description = RichTextField(verbose_name="Opis wydarzenia")
    image = models.ImageField(upload_to='event/%Y/%m/%d/', blank=True, null=True, verbose_name="Plakat")
    place = models.CharField(max_length=120, verbose_name="Miejsce")
    #point = models.PointField(blank=True, null=True, verbose_name="Miejsce na mapie")
    orgs = models.ManyToManyField('Organizer', blank=True, related_name='events', verbose_name="Organizator")
    user = models.ForeignKey(User, blank=True, null=True, related_name='event', verbose_name='Użytkownik')

    category = models.ForeignKey('Category', blank=True, null=True, verbose_name="Kategoria")

    url = models.URLField(blank=True, null=True,verbose_name="Adres www")

    def __str__(self):
        return self.title


class Category(models.Model):
    COLORS = (
        ('panel-primary', 'Niebieski'),
        ('panel-success', 'Zielony'),
        ('panel-info', 'Jasno niebieski'),
        ('panel-warning', 'Żółty'),
        ('panel-danger', 'Czerwony'),
    )
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=16, choices=COLORS, default="panel-primary")

    def __str__(self):
        return self.name


class Organizer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nazwa")
    logo = models.ImageField(upload_to='logo/%m/', blank=True, null=True, verbose_name="Logo")
    user = models.OneToOneField(User, blank=True, null=True, related_name='organizer', verbose_name="Użytkownik")

    def __str__(self):
        return self.name
