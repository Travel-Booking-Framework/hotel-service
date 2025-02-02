from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

    def validate_price_per_night(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value