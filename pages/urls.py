"""
URL configuration for saloonweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin,staticfiles
from django.urls import path,include
from pages import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('about/', views.about, name="about" ),
    path('contact/', views.contact, name="contact" ),
    path('reviews/', views.reviews, name="reviews" ),
    path('services/', views.services, name="services" ),
    path('gallery/', views.gallery, name="gallery" ),
    
    
    
    path('services/<service_slug>/', views.service_view, name="services" ),
    path('page/<page_slug>/', views.pages_view, name="pages" ),
    path('page-json/<category>/<page_slug>/', views.json_pages_view, name="jsonpages" ),
]