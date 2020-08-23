from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add=True)
    birthday = models.DateTimeField()
    def __str__(self):
        return self.username