from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    img_profile_url = models.URLField(blank=True, default='')
    nickname = models.CharField(blank=True, max_length=100)
