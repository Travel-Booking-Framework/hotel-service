from pybreaker import CircuitBreaker
from .repository import HotelRepository

hotel_breaker = CircuitBreaker(fail_max=3, reset_timeout=60)

class CreateHotelCommand:
    def __init__(self, data):
        self.data = data

    @hotel_breaker
    def execute(self):
        return HotelRepository.create_hotel(self.data)

class UpdateHotelCommand:
    def __init__(self, hotel_id, data):
        self.hotel_id = hotel_id
        self.data = data

    @hotel_breaker
    def execute(self):
        return HotelRepository.update_hotel(self.hotel_id, self.data)

class DeleteHotelCommand:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    @hotel_breaker
    def execute(self):
        return HotelRepository.delete_hotel