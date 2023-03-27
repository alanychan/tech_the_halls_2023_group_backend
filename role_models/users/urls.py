from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view(), name='customusers-list'),
    path('users/<int:pk>', views.CustomUserDetail.as_view(), name='customusers-detail'),

    path('category/', views.CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='category-detail'),
    
    path('questions/', views.QuestionList.as_view(), name='questions-list'),
    path('questions/<int:pk>', views.QuestionDetail.as_view(), name='questions-detail'),
    
    path('users-answers/', views.AnswerList.as_view(), name='quetions-answers'),    
]
