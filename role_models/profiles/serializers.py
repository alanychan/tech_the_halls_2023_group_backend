from rest_framework import serializers

class ProfilesSerializer(serializers.Serializer):
	name = serializers.ReadOnlyField()
	title = serializers.CharField(max_length=200)
	description = serializers.CharField(max_length=None)
	image = serializers.URLField()
	is_open = serializers.BooleanField()
	date_created = serializers.DateTimeField()
	owner = serializers.CharField(max_length=200)
