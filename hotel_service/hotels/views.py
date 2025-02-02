from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import HotelSerializer
from .commands import CreateHotelCommand, UpdateHotelCommand, DeleteHotelCommand, BookHotelCommand

class HotelListView(APIView):
    def get(self, request):
        return Response("List of hotels")
    
    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            command = CreateHotelCommand(serializer.validated_data)
            return Response("Create a hotel", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HotelDetailView(APIView):
    def get(self, request, hotel_id):
        return Response(f"Details of hotel {hotel_id}")
    
    def put(self, request, hotel_id):
        serializer = HotelSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            command = UpdateHotelCommand(hotel_id, serializer.validated_data)
            return Response(f"Update hotel {hotel_id}", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, hotel_id):
        command = DeleteHotelCommand(hotel_id)
        return Response(f"Delete hotel {hotel_id}", status=status.HTTP_204_NO_CONTENT)

class HotelBookingView(APIView):
    def post(self, request, hotel_id):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            command = BookHotelCommand(hotel_id, serializer.validated_data)
            return Response(f"Book hotel {hotel_id}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
