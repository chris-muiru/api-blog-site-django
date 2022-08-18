from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", ]

# Register your models here.

# Create your models here.
