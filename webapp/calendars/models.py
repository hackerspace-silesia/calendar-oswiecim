from django.db import models


class Event(models.Model):
    start_time = models.DateTimeField(verbose_name="Start wydarzenia")
    end_time = models.DateTimeField(blank=True, null=True, verbose_name="Koniec wydarzenia")
    title = models.CharField(max_length=120, verbose_name="Tytuł")
    description = models.TextField(verbose_name="Opis")
    image = models.ImageField(upload_to='event/%Y/%m/%d/', blank=True, null=True, verbose_name="Plakat")

    def __str__(self):
        return self.title


class Organizer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nazwa")
    logo = models.ImageField(upload_to='logo/%m/', blank=True, null=True, verbose_name="Logo")

    def __str__(self):
        return self.name
