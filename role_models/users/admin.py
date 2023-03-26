from django.contrib import admin
from .import models

# Register your models here.
admin.site.register(models.CustomUser)
admin.site.register(models.Category)
admin.site.register(models.Questions)
admin.site.register(models.User_Answers)
#register link
admin.site.site_url = "/users"
admin.site.site_url = "/category"
admin.site.site_url = "/questions"
admin.site.site_url = "/answers"