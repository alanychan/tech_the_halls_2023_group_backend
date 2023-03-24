from rest_framework import serializers
from .models import Profiles

class ProfilesSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	title = serializers.CharField(max_length=200)
	description = serializers.CharField(max_length=None)
	image = serializers.URLField()
	is_open = serializers.BooleanField()
	date_created = serializers.DateTimeField()
	owner = serializers.CharField(max_length=200)
