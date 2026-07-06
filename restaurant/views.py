from rest_framework import generics
from django.shortcuts import render
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

def home(request):
    return render(request, 'index.html')

class MenuListCreateView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
