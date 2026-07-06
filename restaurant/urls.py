from django.urls import path
from .views import MenuListCreateView, BookingListCreateView

urlpatterns = [
    path('menu/', MenuListCreateView.as_view()),
    path('booking/', BookingListCreateView.as_view()),
]
