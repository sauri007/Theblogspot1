from django.contrib import admin
from django.urls import path
from account import views



urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("userlogin/", views.userlogin, name="userlogin"),
    path("userlogout/", views.userlogout, name="userlogout"),


]