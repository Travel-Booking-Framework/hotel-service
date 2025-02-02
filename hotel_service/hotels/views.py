from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .repository import HotelRepository
from .serializers import HotelSerializer
from .grpc_client import HotelClient

class HotelListView(APIView):
    def get(self, request):
        hotels = HotelRepository.get_all_hotels()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            hotel = HotelRepository.create_hotel(serializer.validated_data)
            return Response(HotelSerializer(hotel).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HotelDetailView(APIView):
    def get(self, request, hotel_id):
        hotel = HotelRepository.get_hotel_by_id(hotel_id)
        if not hotel:
            return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)

    def put(self, request, hotel_id):
        hotel = HotelRepository.get_hotel_by_id(hotel_id)
        if not hotel:
            return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = HotelSerializer(hotel, data=request.data, partial=True)
        if serializer.is_valid():
            updated_hotel = HotelRepository.update_hotel(hotel, serializer.validated_data)
            return Response(HotelSerializer(updated_hotel).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, hotel_id):
        if not HotelRepository.get_hotel_by_id(hotel_id):
            return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)
        
        HotelRepository.delete_hotel(hotel_id)
        return Response({'message': 'Hotel deleted'}, status=status.HTTP_204_NO_CONTENT)

class HotelBookingView(APIView):
    def post(self, request, hotel_id):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not HotelRepository.get_hotel_by_id(hotel_id):
            return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)
        
        client = HotelClient()
        try:
            response = client.book_hotel(user_id, hotel_id)
            return Response({'message': response.message})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)