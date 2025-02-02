from .models import Hotel

class HotelRepository:
    @staticmethod
    def get_all_hotels():
        return Hotel.objects.all()

    @staticmethod
    def get_hotel_by_id(hotel_id):
        return Hotel.objects.filter(id=hotel_id).first()

    @staticmethod
    def create_hotel(data):
        return Hotel.objects.create(**data)

    @staticmethod
    def update_hotel(hotel_id, data):
        Hotel.objects.filter(id=hotel_id).update(**data)

    @staticmethod
    def delete_hotel(hotel_id):
        Hotel.objects.filter(id=hotel_id).delete()
