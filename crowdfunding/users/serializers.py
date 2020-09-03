from rest_framework import serializers
from .models import CustomUser, Profile
from projects.serializers import PledgeSerializer,ProjectSerializer


# class CustomUserSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     username = serializers.CharField(max_length=200)
#     email = serializers.CharField(max_length=200)
#     preferred_name = serializers.CharField(max_length=200)
#     city = serializers.CharField(max_length=200)
#     location = serializers.CharField(max_length=200)
#     date_joined = serializers.ReadOnlyField()
#     display_picture = serializers.URLField()
#     password = serializers.CharField(write_only=True)

#     def create(self, validated_data):
#         new_user = CustomUser.objects.create(**validated_data)
#         new_user.set_password(validated_data['password'])
#         new_user.save()
#         return new_user
        

# class CustomUserDetailSerializer(CustomUserSerializer):
#     def update(self, instance, validated_data):
#         instance.preferred_name = validated_data.get('preferred_name',instance.preferred_name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.password = validated_data.get('password', instance.password)
#         instance.city = validated_data.get('city', instance.city)
#         instance.location = validated_data.get('location', instance.location)
#         instance.display_picture = validated_data.get('display_picture', instance.display_picture)
#         instance.date_joined = validated_data.get('date_joined', instance.date_joined)
#         instance.last_updated = validated_data.get('last_updated', instance.last_updated)
#         instance.save()
#         return instance



# class CustomUserDetailSerializer(CustomUserSerializer):
#     def update(self, instance, validated_data):
#         instance.preferred_name = validated_data.get('preferred_name',instance.preferred_name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.password = validated_data.get('password', instance.password)
#         instance.city = validated_data.get('city', instance.city)
#         instance.location = validated_data.get('location', instance.location)
#         instance.save()
#         return instance


# class ProfileSerializer(serializers.ModelSerializer):
#     def update(self, instance, validated_data):
#         instance.display_picture = validated_data.get('display_picture', instance.display_picture)
#         instance.date_joined = validated_data.get('date_joined', instance.date_joined)
#         instance.last_updated = validated_data.get('last_updated', instance.last_updated)
#         instance.save()
#         return instance

#     class Meta:
#         model = PublicProfile
#         fields = "__all__"



class ProfileSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=200,required=False)
    location = serializers.CharField(max_length=200,required=False)
    date_joined = serializers.ReadOnlyField()
    last_updated = serializers.ReadOnlyField()
    display_picture = serializers.URLField(required=False)

class CustomUserSerializer(serializers.ModelSerializer):
    userprofile = ProfileSerializer()
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    preferred_name = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=100,write_only=True,required=True,style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password','preferred_name', 'userprofile']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        userprofile_data = validated_data.pop('userprofile')
        new_user = CustomUser.objects.create(**validated_data)
        Profile.objects.create(user=new_user, **userprofile_data)
        new_user.set_password(password)
        new_user.save()
        return new_user

    def update(self, instance, validated_data):
        userprofile_data = validated_data.pop('userprofile')
        try:
            userprofile = instance.userprofile
        except CustomUser.userprofile.RelatedObjectDoesNotExist:
            userprofile = Profile.objects.create(user=instance, **userprofile_data)

        instance.id = validated_data.get('id', instance.id)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.preferred_name = validated_data.get('preferred_name',instance.preferred_name)
        instance.password = validated_data.get('password', instance.password)
        instance.save()

        userprofile.date_joined = userprofile_data.get(
            'date_joined',
            userprofile.date_joined
        )
        userprofile.last_updated = userprofile_data.get(
            'last_updated',
            userprofile.last_updated
        )
        userprofile.city = userprofile_data.get(
            'city',
            userprofile.city
        )
        userprofile.location = userprofile_data.get(
            'location',
            userprofile.location
        )
        userprofile.display_picture = userprofile_data.get(
            'display_picture',
            userprofile.display_picture
        )
        userprofile.save()
        return instance

        



class CustomUserActivitySerializer(CustomUserSerializer):
    owner_projects = ProjectSerializer(many=True, read_only=True)
    supporter_pledges = PledgeSerializer(many=True, read_only=True)
    count_pledged = serializers.SerializerMethodField()
    count_projects = serializers.SerializerMethodField()
    def get_count_pledged(self, obj):
        return obj.supporter_pledges.count()
    
    def get_count_projects(self, obj):
        return obj.owner_projects.count()
