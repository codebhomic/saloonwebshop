from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Appointment, Offer
from pages.models import Content, Category
from .forms import AppointmentForm
from django.contrib import messages
from pages.functions import paginate
from datetime import datetime,date
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if not request.user.is_authenticated:
        return render(template_name="asklogin.html",request=request)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment_date = datetime.strftime(form.cleaned_data["appointment_date"],'%Y%m%d')
            today = datetime.strftime(datetime.today(),'%Y%m%d')
            start_time = str(form.cleaned_data["start_time"]).replace(":","")
            time = datetime.strftime(datetime.today(),'%H%M%S')
            if(today > appointment_date):
                if(today > appointment_date):
                    form.add_error("appointment_date","Please Book appointment for future Dates")
                    form.add_error("start_time","Please Book appointment for future Times")
            elif((today == appointment_date) and (time > start_time)):
                form.add_error("start_time","Please Book appointment for future Times")
            else:
                appointment = form.save(commit=False)
                appointment.user = request.user
                if not appointment.is_conflicting(form.cleaned_data['services']):
                    appointment.save()
                    form.save_m2m()  # Save many-to-many relationships
                    messages.success(request=request,message="Your Appointment is Booked")
                    return redirect('appointments')
                else:
                    form.add_error("start_time", "This time slot is already booked. Please choose another time.")
    else:
        form = AppointmentForm()
    context = {
        "title":"Book Appointment",
        'form': form,
    }
    return render(request,"booking.html",context)

@login_required
def appointment_success(request):
    context = {
        "title":"Appointment Success",
    }
    return render(request, 'appointment_success.html',context=context)

def offers_view(request):
    offers = Offer.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())
    context = {
        "title":"offers",
        'offers': offers
    }
    return render(request, 'offers.html',context=context)

def appointments(request):
    appointments = Appointment.objects.filter(user=request.user).order_by('appointment_date')
    appointments = paginate(appointments,request.GET.get('page'),9)
    context = {
        "title":"appointments",
        'bookings': appointments
    }
    return render(request, 'appointments.html',context=context)

@csrf_exempt
def toggle_booking(request, booking_id):
    if request.method == 'POST':
        try:
            booking = Appointment.objects.get(id=booking_id)
            new_status = 'canceled' if booking.status == 'pending' else 'pending'
            booking.status = new_status
            booking.save()
            return JsonResponse({'message': f'Booking status updated to {new_status}'}, status=200)
        except Appointment.DoesNotExist:
            return JsonResponse({'error': 'Booking not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)