from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
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

    tagline = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    profile_pic = models.URLField(blank=True)
    video = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    blog = models.URLField(blank=True)
    job_title = models.CharField(max_length=200, blank=True)
    featured = models.BooleanField(default=False)
    pronouns = models.CharField(max_length=200, blank=True)

    is_published = models.BooleanField(default=False)

    categories = models.ManyToManyField(Category, related_name="categories", blank=True)

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
    answer = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.answer}"
