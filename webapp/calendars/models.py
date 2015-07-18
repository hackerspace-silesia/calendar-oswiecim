from django.db import models

# Create your models here.

class Event(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title


class Organizer(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo/%m/')

    def __str__(self):
        return self.name
