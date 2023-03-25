from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hero
from .serializers import HeroSerializer

from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import permissions

# Create your views here.
class HeroList(APIView):

    def get(self, request):
        hero = Hero.objects.all()
        serializer = HeroSerializer(hero, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
            status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['GET', 'PUT', 'DELETE'])
def hero_detail_view(request, pk):
    # permission_classes = [permissions.IsAdminUser]

    try:
        hero = Hero.objects.get(pk=pk)
    except Hero.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HeroSerializer(hero)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HeroSerializer(hero, data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
