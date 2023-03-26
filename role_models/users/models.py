from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Questions(models.Model):
    question = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question   
    
class CustomUser(AbstractUser):
    categories = models.ManyToManyField(Category, related_name="categories")
    questions = models.ManyToManyField(Questions, through='User_Answers')
    
    def __str__(self):
        return self.username

class User_Answers(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.answer}"

# class UserAnswer(models.Model):
#     customUser = models.ForeignKey(CustomUser, related_name='answers', on_delete=models.CASCADE)
#     answer = models.ForeignKey(Answer, related_name='user_answers', on_delete=models.CASCADE)
    
#     def __str__(self):
#             return self.answer
