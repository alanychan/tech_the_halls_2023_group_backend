from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Category, CustomUser, Question, Answer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CustomUserCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser.categories.through
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Question
        fields = '__all__'
        
class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'

class CustomUserSerializer(serializers.Serializer):
    categories = CategorySerializer(many=True, read_only=True)
    user_answers = AnswerSerializer(many=True, read_only=True)
    question_answers = AnswerSerializer(many=True, read_only=True)
    
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only = True, required = True , validators =[validate_password])
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}, "id": {"read_only": True}, 'first_name': {'required': True},'last_name': {'required': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(
          email = validated_data['email'],
          username = validated_data['username'],
          first_name = validated_data['first_name'],
          last_name = validated_data['last_name'],
          tagline = validated_data['tagline'],
          city = validated_data['city'],
          country = validated_data['country'],
          profile_pic = validated_data['profile_pic'],
          video = validated_data['video'],
          linkedin = validated_data['linkedin'],
          twitter = validated_data['twitter'],
          blog = validated_data['blog'],
          job_title = validated_data['blog'],
          featured = validated_data['featured'],
          pronouns = validated_data['pronouns']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user    
     
class CustomUserDetailSerializer(CustomUserSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'categories', 'user_answers']
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        # instance.categories = validated_data.get('categories', instance.categories)
        # instance.user_answers = validated_data.get('user_answers', instance.user_answers)
        
        
        if password := validated_data.get('password'):
            instance.set_password(password)

        # instance.set_password(validated_data['password'])

        instance.save()
        return instance

    