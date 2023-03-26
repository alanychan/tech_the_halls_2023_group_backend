from rest_framework import serializers
from .models import Category, CustomUser, Questions, User_Answers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
# class CustomUserCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser.categories.through
#         fields = "__all__"

    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {"password":{"write_only":True}}

class QuestionsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Questions
        fields = '__all__'
        
class User_AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Answers
        fields = '__all__'
        
class CustomUserDetailSerializer(CustomUserSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    answers = User_AnswersSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'categories', 'questions', 'answers']
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.questios = validated_data.get('questions', instance.questions)
        instance.answers = validated_data.get('answers', instance.answers)
        
        if password := validated_data.get('password'):
            instance.set_password(password)

        # instance.set_password(validated_data['password'])

        instance.save()
        return instance

    