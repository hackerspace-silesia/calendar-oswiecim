from ckeditor.fields import RichTextField
from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    start_time = models.DateTimeField(verbose_name="Start wydarzenia")
    end_time = models.DateTimeField(blank=True, null=True, verbose_name="Koniec wydarzenia")
    title = models.CharField(max_length=120, verbose_name="Tytuł")
    description = RichTextField()
    image = models.ImageField(upload_to='event/%Y/%m/%d/', blank=True, null=True, verbose_name="Plakat")
    place = models.CharField(max_length=120, verbose_name="Miejsce")
    point = models.PointField(blank=True, null=True, verbose_name="Miejsce na mapie")

    objects = models.GeoManager()

    def __str__(self):
        return self.title


class Organizer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nazwa")
    logo = models.ImageField(upload_to='logo/%m/', blank=True, null=True, verbose_name="Logo")
    user = models.ForeignKey(User, null=True)
    events = models.ManyToManyField(Event)

    def __str__(self):
        return self.name
