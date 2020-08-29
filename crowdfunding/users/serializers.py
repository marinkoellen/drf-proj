from rest_framework import serializers
from .models import CustomUser
from projects.serializers import PledgeSerializer,ProjectSerializer


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    preferred_name = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=200)
    location = serializers.CharField(max_length=200)
    date_joined = serializers.ReadOnlyField()
    birthday = serializers.DateTimeField()
    display_picture = serializers.URLField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        new_user = CustomUser.objects.create(**validated_data)
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user
        

class CustomUserDetailSerializer(CustomUserSerializer):
    owner_projects = ProjectSerializer(many=True, read_only=True)
    supporter_pledges = PledgeSerializer(many=True, read_only=True)
    
    def update(self, instance, validated_data):
        instance.preferred_name = validated_data.get('preferred_name',instance.preferred_name)
        instance.city = validated_data.get('city', instance.city)
        instance.location = validated_data.get('location', instance.location)
        instance.email = validated_data.get('email', instance.email)
        instance.display_picture = validated_data.get('display_picture', instance.display_picture)
        instance.password = validated_data.get('password', instance.password)

        instance.save()
        return instance

