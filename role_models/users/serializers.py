from rest_framework import serializers
from .models import Category, CustomUser

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser.user_categories.through
        fields = "__all__"

class CustomUserDetailSerializer(CustomUserSerializer):
    categories = CategorySerializer(many=True, read_only=True)
