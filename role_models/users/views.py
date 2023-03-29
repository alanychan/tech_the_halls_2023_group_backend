from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework import status, permissions, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from .serializers import CustomUserSerializer, CustomUserDetailSerializer, CategorySerializer, CustomUserCategorySerializer
from .serializers import QuestionSerializer, AnswerSerializer
from .models import CustomUser, Category, Question, Answer

# Create your views here.
class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    
    # def perform_create(self, serializer):
    #     serializer.save()

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class CustomUserCategoryList(generics.ListCreateAPIView):
    queryset = CustomUser.categories.through.objects.all()
    serializer_class = CustomUserCategorySerializer
    
class CustomUserCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.categories.through.objects.all()
    serializer_class = CustomUserCategorySerializer

class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class CustomUserDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserDetailSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserDetailSerializer(
            instance=user, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserDetailSerializer(instance=user, data=data)

        if serializer.is_valid:
            user.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

