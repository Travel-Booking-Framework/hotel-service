from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    available_rooms = models.IntegerField()


    def __str__(self):
        return f"{self.name} Hotel"