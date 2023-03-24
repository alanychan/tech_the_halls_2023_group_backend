from django.shortcuts import render
from rest_framework import status, permissions, generics

from .serializers import CustomUserSerializer, CategorySerializer, CustomUserCategorySerializer
from .models import CustomUser, Category


# Create your views here.
class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def perform_create(self, serializer):
        serializer.save()


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CustomUserCategoryList(generics.ListCreateAPIView):
    queryset = CustomUser.user_categories.through.objects.all()
    serializer_class = CustomUserCategorySerializer

class CustomUserCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.user_categories.through.objects.all()
    serializer_class = CustomUserCategorySerializer

