from django.contrib import admin
from .models import CustomUser,CustomUserAdmin





admin.site.register(CustomUser, CustomUserAdmin)
