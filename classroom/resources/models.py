from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

class Schedule(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    booked_by = models.CharField(max_length=255)

class Maintenance(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    maintenance_date = models.DateTimeField()
    description = models.TextField()