from django.contrib.auth.models import AbstractUser, User
from django.db import models

class SiteUser(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)


class ProfileUser1(models.Model):
    user = models.OneToOneField(SiteUser, on_delete=models.CASCADE, primary_key=True)


class ProfileUser2(models.Model):
    user = models.OneToOneField(SiteUser, on_delete=models.CASCADE, primary_key=True)
