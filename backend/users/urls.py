from django.contrib import admin
from django.urls import path, include

from backend.users.views import CustomUserRegisterView


app_name = "users"

urlpatterns = [
    path("register/", CustomUserRegisterView.as_view(), name="register"),
]
