from django.urls import path
from . import views

urlpatterns = [
    path('api/bookings/', views.booking_list),
    path('api/bookings/<int:pk>/', views.booking_detail),
    path('api/registration/', views.registration),
    # Add more API paths as needed
]
