from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=200)
    location = serializers.CharField(max_length=200)
    date_joined = serializers.ReadOnlyField()
    birthday = serializers.DateTimeField()
    display_picture = serializers.URLField()
    project_preferences = serializers.CharField(max_length=200)


    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)


class CustomUserDetailSerializer(CustomUserSerializer):
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('description',instance.last_name)
        instance.city = validated_data.get('city', instance.city)
        instance.location = validated_data.get('location', instance.location)
        instance.email = validated_data.get('email', instance.email)
        instance.display_picture = validated_data.get('display_picture', instance.display_picture)
        instance.project_preferences = validated_data.get('project_preferences', instance.project_preferences)

        instance.save()
        return instance

