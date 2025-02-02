from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available_rooms = models.IntegerField()


    def __str__(self):
        return f"{self.name} Hotel"


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return f"Image for {self.hotel.name}"