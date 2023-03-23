from django.shortcuts import render
from rest_framework import status, permissions, generics

from .serializers import CustomUserSerializer
from .models import CustomUser

# Create your views here.
class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def perform_create(self, serializer):
        serializer.save()