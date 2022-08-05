from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  # create a student if nothing is given to level
  level = models.IntegerField(editable=False, default=200)