from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, min_value=0)
    available_rooms = models.IntegerField()


    def __str__(self):
        return f"{self.name} Hotel"