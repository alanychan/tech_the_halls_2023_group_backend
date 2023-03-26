from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from .serializers import CustomUserSerializer, CustomUserDetailSerializer, CategorySerializer, QuestionsSerializer
from .serializers import User_AnswersSerializer
from .models import CustomUser, Category, Questions, User_Answers

# Create your views here.
class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def perform_create(self, serializer):
        serializer.save()

# class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class CustomUserCategoryList(generics.ListCreateAPIView):
#     queryset = CustomUser.categories.through.objects.all()
#     serializer_class = CustomUserCategorySerializer

# class CustomUserCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CustomUser.categories.through.objects.all()
#     serializer_class = CustomUserCategorySerializer

class QuestionsList(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class QuestionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class User_AnswersList(generics.ListCreateAPIView):
    queryset = User_Answers.objects.all()
    serializer_class = User_AnswersSerializer

class User_AnswersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_Answers.objects.all()
    serializer_class = User_AnswersSerializer

class UserAnswersView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        user_answers = User_Answers.objects.filter(user=user)
        serializer = User_AnswersSerializer(user_answers, many=True)
        return Response(serializer.data)

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
        serializer = CustomUserSerializer(instance=user, data=data)

        if serializer.is_valid:
            user.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

