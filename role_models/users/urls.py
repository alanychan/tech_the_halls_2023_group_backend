from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view(), name='customusers-list'),
    path('users/<int:pk>', views.CustomUserDetail.as_view(), name='users-detail'),

    path('category/', views.CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='category-detail'),
    
    path('user-categories/', views.CustomUserCategoryList.as_view(), name='user-category-list'),
    path('user-categories/<int:pk>', views.CustomUserCategoryDetail.as_view(), name='user-category-detail'),
]
