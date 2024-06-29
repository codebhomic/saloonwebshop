from django.db import models
from django.contrib.auth.models import User
from pages.models import Content
from django.utils import timezone
from datetime import datetime,date
from django.utils.timezone import timedelta

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
        ('reject', 'Reject'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    services = models.ManyToManyField(Content, limit_choices_to={'category__name': 'Services'})
    appointment_date = models.DateField()
    start_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} on {self.appointment_date} at {self.start_time}"

    def get_end_time(self,services):
        # print()
        total_duration = sum([self.parse_duration(service.duration) for service in services], timedelta())
        start_datetime = datetime.combine(date.today(), self.start_time)
        end_datetime = start_datetime + total_duration
        return end_datetime.time()

    def parse_duration(self, duration_str):
        # This method converts a string like "30 minutes" into a timedelta
        duration_str = duration_str.lower()
        if 'hour' in duration_str:
            hours = int(duration_str.split()[0])
            return timedelta(hours=hours)
        elif 'minute' in duration_str:
            minutes = int(duration_str.split()[0])
            return timedelta(minutes=minutes)
        else:
            return timedelta()
    
    def is_conflicting(self,services):
        end_time = self.get_end_time(services)
        start_datetime = datetime.combine(self.appointment_date, self.start_time)
        end_datetime = datetime.combine(self.appointment_date, end_time)
        overlapping_appointments = Appointment.objects.filter(
            appointment_date=self.appointment_date,
            start_time__lt=end_datetime.time(),
            status__in=['pending', 'confirmed']
        ).exclude(id=self.id)
        # print(overlapping_appointments)
        # return True
        return overlapping_appointments.exists()


class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    services = models.ManyToManyField(Content, limit_choices_to={'category__name': 'Services'})
    
    def __str__(self):
        return self.title

    def is_active(self):
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date
