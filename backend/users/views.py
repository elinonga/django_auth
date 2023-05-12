from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from backend.users.serializers import CustomUserRegisterSerializer

# Create your views here.


class CustomUserRegisterView(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = CustomUserRegisterSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)
