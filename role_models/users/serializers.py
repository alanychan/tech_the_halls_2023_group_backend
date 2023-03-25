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

class CustomUserDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        
        if password := validated_data.get('password'):
            instance.set_password(password)

        # instance.set_password(validated_data['password'])

        instance.save()
        return instance
