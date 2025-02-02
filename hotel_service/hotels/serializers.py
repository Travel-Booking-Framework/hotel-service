from rest_framework import serializers
from .models import Hotel, HotelImage

class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['id', 'image_url']

class HotelSerializer(serializers.ModelSerializer):
    images = HotelImageSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'address', 'rating', 'images']

    def validate_price_per_night(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value
