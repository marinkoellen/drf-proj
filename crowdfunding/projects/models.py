from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.utils.timezone import timezone, timedelta

class Category(models.Model):
    name = models.CharField(max_length=250,unique=True)
    def __str__(self):
        return self.name


# Create your models here.
def get_closing_date():
    return datetime.today() + timedelta(days=60)

class Like(models.Model):
    liker = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='liker'
    )

    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='user_likes'
    )

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    dream_goal = models.IntegerField()
    campaign_end_date = models.DateTimeField(default=get_closing_date)
    image = models.URLField(blank=True,null=True)
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

    city = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    proj_cat = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, related_name='project_categories') 

    @property
    def total_pledges(self):
        pledges = Pledge.objects.filter(project = self.id)
        pledge_total = 0
        for pledge in pledges:
            pledge_total = pledge_total + pledge.amount 
        return pledge_total
    @property
    def total_likes(self):
        # likes = Like.objects.filter(project = self.id).distinct('liker')
        likes = Like.objects.filter(project = self.id)
        like_total = 0
        for like_i in likes:
            like_total = like_total + 1
        return like_total
    
  
    # def save(self,*args,**kwargs):
    #     if self.total_pledges() >= self.dream_goal:
    #         self.is_open = False
    #         self.campaign_end_date = datetime.today()
    #     models.Model.save(self,*args,**kwargs)



class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )

    date_pledged = models.DateTimeField(auto_now_add=True)


