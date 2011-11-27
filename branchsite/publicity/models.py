from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    location_name = models.CharField(max_length=30)
    location_address = models.CharField(max_length=100, blank=True, null=True)
    location_directions = models.CharField(max_length=100, blank=True, null=True)
    start = models.DateTimeField()
    duration_hours = models.FloatField(blank=True, null=True)


