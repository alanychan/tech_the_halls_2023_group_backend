from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Question(models.Model):
    question = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question   
    
class CustomUser(AbstractUser):
    categories = models.ManyToManyField(Category, related_name="categories")
    
    def __str__(self):
        return self.username

class Answer(models.Model):
    user = models.ForeignKey(
        CustomUser, 
        related_name="user_answers", 
        on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, 
        related_name='questions_answers', 
        on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.answer}"
