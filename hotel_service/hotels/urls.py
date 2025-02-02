from django.urls import path
from .views import HotelListView, HotelDetailView, HotelBookingView

urlpatterns = [
    path('hotels/', HotelListView.as_view(), name='hotel-list'),
    path('hotels/<int:hotel_id>/', HotelDetailView.as_view(), name='hotel-detail'),
    path('hotels/<int:hotel_id>/book/', HotelBookingView.as_view(), name='hotel-booking'),
]
