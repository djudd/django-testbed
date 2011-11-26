from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=100)
    description = models.TextField()
    location_name = models.CharField(max_length=30)
    location_address = models.CharField(max_length=100)
    start = models.DateTimeField()
    duration_hours = models.FloatField()


