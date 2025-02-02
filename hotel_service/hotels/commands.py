from .repository import HotelRepository

class HotelCommands:
    @staticmethod
    def create_hotel(data):
        return HotelRepository.create_hotel(data)

    @staticmethod
    def update_hotel(hotel_id, data):
        return HotelRepository.update_hotel(hotel_id, data)

    @staticmethod
    def delete_hotel(hotel_id):
        return HotelRepository.delete_hotel(hotel_id)
