from django.urls import path, include
from restaurant.views import home

urlpatterns = [
    path('', home),
    path('api/', include('restaurant.urls')),
]
