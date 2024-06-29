from django.contrib import admin,staticfiles
from django.urls import path,include
from users import views

urlpatterns = [
    path('signup/',views.signup, name="signup"),
    path('signin/',views.signin, name="signin"),
    path('signout/',views.signout, name="signout"),
    path('reviews/',views.reviews, name="reviews"),
    path('profile/',views.profile, name="profile"),
    path('profile/change-password/',views.changepassword, name="ChangePassword"),
    path('profile/change-details/',views.changedetails, name="ChangeDetails"),
]
