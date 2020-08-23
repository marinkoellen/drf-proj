from django.db import models
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model

# Create your models here.
def get_closing_date():
    return datetime.today() + timedelta(days=60)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    dream_goal = models.IntegerField()
    campaign_end_date = models.DateTimeField(default=get_closing_date)
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

    city = models.CharField(max_length=200)
    location = models.CharField(max_length=200)



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
