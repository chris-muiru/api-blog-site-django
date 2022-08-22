from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", ]

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields': (
                    'is_writter',
                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)
