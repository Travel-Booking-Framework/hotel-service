from rest_framework.response import Response
from rest_framework.views import APIView
from .repository import HotelRepository
from .commands import HotelCommands
from .grpc_client import HotelClient

class HotelListView(APIView):
    def get(self, request):
        hotels = HotelRepository.get_all_hotels()
        data = [{'id': h.id, 'name': h.name, 'location': h.location, 'available_rooms': h.available_rooms} for h in hotels]
        return Response(data)

    def post(self, request):
        hotel = HotelCommands.create_hotel(request.data)
        return Response({'id': hotel.id, 'name': hotel.name, 'location': hotel.location, 'available_rooms': hotel.available_rooms})

class HotelDetailView(APIView):
    def get(self, request, hotel_id):
        hotel = HotelRepository.get_hotel_by_id(hotel_id)
        if hotel:
            return Response({'id': hotel.id, 'name': hotel.name, 'location': hotel.location, 'available_rooms': hotel.available_rooms})
        return Response({'error': 'Hotel not found'}, status=404)

    def put(self, request, hotel_id):
        HotelCommands.update_hotel(hotel_id, request.data)
        return Response({'message': 'Hotel updated'})

    def delete(self, request, hotel_id):
        HotelCommands.delete_hotel(hotel_id)
        return Response({'message': 'Hotel deleted'})

class HotelBookingView(APIView):
    def post(self, request, hotel_id):
        user_id = request.data.get('user_id')
        client = HotelClient()
        response = client.book_hotel(user_id, hotel_id)
        return Response({'message': response.message})