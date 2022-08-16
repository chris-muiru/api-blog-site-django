from fileinput import isstdin
from django.db import models
from django.contrib.auth.models import User


class WritterModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isStaff = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now=True)
