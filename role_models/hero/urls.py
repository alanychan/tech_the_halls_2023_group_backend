from django.urls import path
from . import views

urlpatterns = [
	path('hero/', views.HeroList.as_view(), name='hero-list'),
    path('hero/<int:pk>', views.hero_detail_view),
]
