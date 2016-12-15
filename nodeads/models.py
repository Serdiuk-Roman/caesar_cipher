from django.db import models

class Culeba(models.Model):
    name = models.CharField(max_length=140)
    lon = models.CharField(max_length=140)
    lat = models.CharField(max_length=140)
    date = models.CharField(max_length=140)
    time = models.CharField(max_length=140)
    temp_max = models.CharField(max_length=140)
    temp_min = models.CharField(max_length=140)
    wind = models.CharField(max_length=140)
    cloud = models.CharField(max_length=140)
    pressure = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    
    def __str__(self):
        return str(self.date) + str(' ') + str(self.time)
