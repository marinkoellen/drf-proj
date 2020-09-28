from rest_framework import serializers
from .models import Project, Pledge, Category, Like
from django.utils.timezone import now


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)



class CategoryDetailSerializer(CategorySerializer):
    lookup_field = 'name'
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    dream_goal = serializers.IntegerField()
    campaign_end_date = serializers.DateTimeField(input_formats=['%Y-%m-%d',])
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='owner.username')
    city = serializers.CharField(max_length=200)
    location = serializers.CharField(max_length=200)
    proj_cat = serializers.SlugRelatedField(
        queryset= Category.objects.all(),
        read_only=False,
        slug_field='name'
     )
    total_pledges = serializers.ReadOnlyField()
    dream_goal_met = serializers.SerializerMethodField()
    total_likes = serializers.ReadOnlyField()
    project_close = serializers.SerializerMethodField()
    goal_met = serializers.SerializerMethodField()

    class Meta:
        model = Project

    def get_goal_met(self, obj):
        if obj.total_pledges > obj.goal:
            return True
        else:
            return False    
    
    def get_dream_goal_met(self, obj):
        if obj.total_pledges > obj.dream_goal:
            return True
        else:
            return False

    def get_project_close(self, obj):
        print(now())
        print(obj.campaign_end_date)
        print(now() > obj.campaign_end_date)
        if now() > obj.campaign_end_date:
            return True
        elif obj.is_open == False:
            return True
        else:
            return False
    
    def create(self, validated_data):
        return Project.objects.create(**validated_data)



class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter = serializers.ReadOnlyField(source='supporter.username')
    project_id = serializers.IntegerField()
    date_pledged = serializers.ReadOnlyField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.dream_goal = validated_data.get('dream_goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open',instance.is_open)
        instance.proj_cat = validated_data.get('proj_cat',instance.proj_cat)
        instance.save()
        return instance

class PledgeDetailSerializer(PledgeSerializer):
    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment',instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.save()
        return instance

class CategoryProjectSerializer(CategorySerializer):
    project_categories = ProjectSerializer(many=True, read_only=True)
    


class LikeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    liker = serializers.ReadOnlyField(source='liker.username')
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Like.objects.create(**validated_data)

