from django.contrib import admin
from booking.models import Appointment,Offer

@admin.register(Appointment)
class Appointment(admin.ModelAdmin):
    list_display = ('user', 'appointment_date', 'start_time', 'status', 'created_at')
    list_filter = ('services__title','services__tags',"appointment_date",'status')
    search_fields = ('user', 'appointment_date', 'status', 'created_at', 'services')

@admin.register(Offer)
class Offer(admin.ModelAdmin):
    list_display = ('title', 'discount_percentage','start_date','end_date')
    list_filter = ('start_date',"end_date",'services')
    search_fields = ('title','services')
