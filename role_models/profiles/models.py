from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()

class Profiles(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField()
   image = models.URLField()
   is_open = models.BooleanField()
   date_created = models.DateTimeField()
   owner = models.ForeignKey(
      	User,
      	on_delete=models.CASCADE,
      	related_name='owner_profiles'
	)
 
