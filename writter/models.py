from fileinput import isstdin
from django.db import models
from django.contrib.auth.models import AbstractUser


class WritterModel(AbstractUser):
    pass