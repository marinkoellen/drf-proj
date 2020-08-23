from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils import Choices

project_cat = Choices('Food Truck', 'Restaurant','Kitchen Gadgets',"Food Products","Pop up Events","Food Tech Apps", "Recipe Books")


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add=True)
    birthday = models.DateTimeField()
    display_picture = models.URLField()
    project_preferences = models.CharField(choices=project_cat, default=project_cat.Restaurant, max_length=50)

    def __str__(self):
        return self.username