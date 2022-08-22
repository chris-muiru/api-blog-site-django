from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    is_writter = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Writter(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
# Register your models here.
