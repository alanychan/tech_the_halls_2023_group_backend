from django.urls import path
from . import views

urlpatterns = [
	path('profiles/', views.ProfilesList.as_view(), name='profiles-list'),
]
