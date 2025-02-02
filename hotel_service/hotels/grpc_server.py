import grpc
from concurrent import futures
import hotels.hotel_pb2 as hotel_pb2
import hotels.hotel_pb2_grpc as hotel_pb2_grpc
from .repository import HotelRepository

class HotelServiceServicer(hotel_pb2_grpc.HotelServiceServicer):
    def BookHotel(self, request, context):
        hotel = HotelRepository.get_hotel_by_id(request.hotel_id)
        if hotel and hotel.available_rooms > 0:
            hotel.available_rooms -= 1
            hotel.save()
            return hotel_pb2.HotelResponse(message="Booking successful")
        return hotel_pb2.HotelResponse(message="Booking failed")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hotel_pb2_grpc.add_HotelServiceServicer_to_server(HotelServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
