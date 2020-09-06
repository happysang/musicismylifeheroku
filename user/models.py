from django.db import models
from django.contrib.auth.models import AbstractUser 

class CustomUser(AbstractUser):
    rapper = models.CharField(max_length = 15, null = True, blank = True)
    phone_number = models.CharField(max_length = 12, null = True, blank = True)