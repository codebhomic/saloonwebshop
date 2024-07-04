from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import timedelta, datetime, date
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class Content(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='uploads/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration = models.CharField(max_length=50, help_text="Duration of the service")  # Changed field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"title: {self.title},image: {self.image},category: {self.category},duration: {self.duration}"
    
class ContactModel(models.Model):
    name = models.CharField(max_length=100,null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=12,null=False)
    services = models.CharField(max_length=100,null=False)
    message = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Name: {self.name}, Email Address: {self.email},Phone Number: {self.phone},Sent At: {self.created_at}"
    