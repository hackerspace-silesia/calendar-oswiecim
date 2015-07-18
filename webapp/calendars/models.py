from django.db import models


class Event(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='event/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.title


class Organizer(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo/%m/', blank=True, null=True)

    def __str__(self):
        return self.name
