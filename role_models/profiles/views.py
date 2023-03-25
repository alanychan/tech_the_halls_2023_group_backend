#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profiles
from .serializers import ProfilesSerializer

# Create your views here.

class ProfilesList(APIView):

    def get(self, request):
        profiles = Profiles.objects.all()
        serializer = ProfilesSerializer(profiles, many=True)
        return Response(serializer.data)