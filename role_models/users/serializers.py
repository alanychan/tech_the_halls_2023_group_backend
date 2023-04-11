from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Category, CustomUser, Question, Answer
from django.contrib.auth.hashers import make_password
# from random import choice
# from string import digits, ascii_letters


# class password_generator():
# def generate_password():
#     password = ''
#     for password_length in range(8):
#         password += choice(digits+ascii_letters)
#     return password

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
    # question = QuestionSerializer()
    # question = serializers.SerializerMethodField()
    class Meta:
        model = Answer
        fields = '__all__'

    # def get_question(self, instance):
    #     return instance.question.question

    # def get_id(self, instance):
    #     return instance.question.id


class CustomUserSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True, required=False, allow_null=True)
    user_answers = AnswerSerializer(many=True, read_only=True, required=False, allow_null=True)
    question_answers = AnswerSerializer(many=True, read_only=True, required=False, allow_null=True)



    id = serializers.ReadOnlyField()

    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    # password = serializers.CharField(write_only = True, required = True , validators =[validate_password])
    password = serializers.CharField(write_only = True, allow_null=True)

    blog = serializers.URLField(max_length=2048, required=False, allow_null=True)
    city = serializers.CharField(max_length=200, required=False, allow_null=True)
    country = serializers.CharField(max_length=200, required=False, allow_null=True)
    featured = serializers.BooleanField(default=False, required=False)
    is_active = serializers.BooleanField(default=False)
    is_published = serializers.BooleanField(default=False, required=False)
    job_title = serializers.CharField(max_length=200, required=False, allow_null=True)
    linkedin = serializers.URLField(max_length=2048, required=False, allow_null=True)
    profile_pic = serializers.URLField(max_length=2048, required=False, allow_null=True)
    pronouns = serializers.CharField(max_length=100, required=False, allow_null=True)
    tagline = serializers.CharField(max_length=1000, required=False, allow_null=True)
    twitter = serializers.URLField(max_length=2048, required=False, allow_null=True)
    video = serializers.URLField(max_length=2048, required=False, allow_null=True)

    class Meta:
        model = CustomUser
        # fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'password', 'tagline', 'city', 'country', 'profile_pic', 'video', 'linkedin', 'twitter', 'blog', 'job_title', 'featured', 'pronouns', 'categories', 'user_answers', 'question_answers', 'is_published', 'is_active']
        extra_kwargs = {'password': {'write_only': True}, "id": {"read_only": True}, 'first_name': {'required': True},'last_name': {'required': True},'username': {'required': True}}


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
          job_title = validated_data['job_title'],
          featured = validated_data['featured'],
          pronouns = validated_data['pronouns'],
          is_published = validated_data['is_published'],
          is_active = validated_data['is_active'],
        )
        # user.password = generate_password()
        # user.password = make_password(user.email)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomUserDetailSerializer(CustomUserSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'
        # fields = ['username', 'first_name', 'last_name', 'email', 'tagline', 'city', 'country', 'profile_pic', 'video', 'linkedin', 'twitter', 'blog', 'job_title', 'featured','pronouns', 'categories', 'user_answers',  'is_published']

    def update(self, instance, validated_data):
        # instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        # instance.email = validated_data.get('email', instance.email)
        instance.tagline = validated_data.get('tagline', instance.tagline)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        instance.video = validated_data.get('video', instance.video)
        instance.linkedin = validated_data.get('linkedin', instance.linkedin)
        instance.twitter = validated_data.get('twitter', instance.twitter)
        instance.blog = validated_data.get('blog', instance.blog)
        instance.job_title = validated_data.get('job_title', instance.job_title)
        instance.featured = validated_data.get('featured', instance.featured)
        instance.pronouns = validated_data.get('pronouns', instance.pronouns)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        if password := validated_data.get('password'):
            instance.set_password(password)

        # instance.set_password(validated_data['password'])

        instance.save()
        return instance
