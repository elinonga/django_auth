from django.contrib import admin

from backend.users.models import CustomUser

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
    )
    list_filter = (
        "is_active",
        "is_staff",
    )
    ordering = ("date_joined",)


admin.site.register(CustomUser, CustomUserAdmin)
