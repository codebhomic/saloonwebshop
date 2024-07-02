from django.contrib import admin,staticfiles
from django.urls import path,include
from courses import views
urlpatterns = [
    path('coursespage/', views.index, name="coursesindex"),
]