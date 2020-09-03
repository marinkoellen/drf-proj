from django.db import models
from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     preferred_name = models.CharField(max_length=200)
#     city = models.CharField(max_length=200)
#     location = models.CharField(max_length=200)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_updated = models.DateTimeField(auto_now=True)
#     display_picture = models.URLField(blank=True,null=True)
#     def __str__(self):
#         return self.username


class CustomUser(AbstractUser):
    preferred_name = models.CharField(max_length=200)
    def __str__(self):
        return self.username


class Profile(models.Model):
    city = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    display_picture = models.URLField(blank=True,null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='userprofile')


