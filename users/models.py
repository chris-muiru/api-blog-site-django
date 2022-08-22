from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_writter = models.BooleanField(default=False)
    def __str__(self):
        return self.username


# Register your models here.

# Create your models here.
