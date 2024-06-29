from django.contrib import admin,staticfiles
from django.urls import path,include
from booking import views

urlpatterns = [
    path('booking/', views.index, name="booking"),
    path('success/', views.appointment_success, name='appointment_success'),
    path('view-appointments/', views.appointments, name='appointments'),
    path('offers/', views.offers_view, name='offers'),
    path('toggle_booking/<int:booking_id>/', views.toggle_booking, name='toggle_booking'),
]
