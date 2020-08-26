from rest_framework import serializers
from .models import Project, Pledge, Category




class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    dream_goal = serializers.IntegerField()
    campaign_end_date = serializers.DateTimeField()
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
    category = ProjectSerializer(many=True, read_only=True)

    
        
