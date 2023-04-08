from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import  IsOwnerOrAdmin, IsAdminOnly
from .serializers import CustomUserSerializer, CustomUserDetailSerializer, CategorySerializer, CustomUserCategorySerializer
from .serializers import QuestionSerializer, AnswerSerializer
from .models import CustomUser, Category, Question, Answer
# from random import choice
# from string import digits, ascii_letters

# Create your views here.

# def passwordGenerator():
#     password = ''
#     for password_length in range(8):
#         password += choice(digits+ascii_letters)
#     return render({password})


class CustomUserList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrAdmin]

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']

    # def perform_create(self, serializer):
    #     serializer.save()

class CategoryList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOnly]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOnly]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def perform_update(self, serializer):
        serializer.save()
class QuestionList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOnly]

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOnly]

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_update(self, serializer):
        serializer.save()

class CustomUserCategoryList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrAdmin]

    queryset = CustomUser.categories.through.objects.all()
    serializer_class = CustomUserCategorySerializer

class CustomUserCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrAdmin]

    queryset = CustomUser.categories.through.objects.all()
    serializer_class = CustomUserCategorySerializer

class AnswerList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrAdmin]

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrAdmin]

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class CustomUserDetail(APIView):
    permission_classes = [IsOwnerOrAdmin]

    def get_object(self, pk):
        try:
            instance = CustomUser.objects.get(pk=pk)
            self.check_object_permissions(self.request,instance)
            return instance
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

