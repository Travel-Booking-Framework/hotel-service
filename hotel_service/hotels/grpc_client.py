import grpc
import hotels.hotel_pb2 as hotel_pb2
import hotels.hotel_pb2_grpc as hotel_pb2_grpc

class HotelClient:
    def book_hotel(self, user_id, hotel_id):
        with grpc.insecure_channel('localhost:50052') as channel:
            stub = hotel_pb2_grpc.HotelServiceStub(channel)
            response = stub.BookHotel(hotel_pb2.HotelRequest(user_id=user_id, hotel_id=hotel_id))
            return response
