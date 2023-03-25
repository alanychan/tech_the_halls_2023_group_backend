from rest_framework import serializers
from .models import Hero


class HeroSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField();
    name = serializers.CharField(max_length=200)
    bio_pic = serializers.URLField()
    bio_text =serializers.CharField(max_length=None)
    bio_url = serializers.URLField()
    featured = serializers.BooleanField()
    date_created = serializers.DateTimeField()

# Check
    def create(self, validated_data):
        return Hero.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.bio_pic = validated_data.get('bio_pic', instance.bio_pic)
        instance.bio_text = validated_data.get('bio_text', instance.bio_text)
        instance.bio_url = validated_data.get('bio_url', instance.bio_url)
        instance.featured = validated_data.get('featured', instance.featured)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.save()
        return instance