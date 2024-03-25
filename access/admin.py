from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    search_fields = ["email", "name"]
    readonly_fields = ["id", "uuid", "created_at", "updated_at"]

    list_display = [
        "email",
        "name",
        "is_active",
        "is_admin",
        "created_at",
    ]

    list_filter = [
        "is_active",
        "is_admin",
    ]

    filter_horizontal = []
    date_hierarchy = "created_at"
    ordering = ["-created_at"]

    add_fieldsets = (
        (
            "Details",
            {
                "fields": [
                    "email",
                    "name",
                    "bio",
                    "password1",
                    "password2",
                ]
            },
        ),
        (
            "Access",
            {"fields": ["is_active", "is_admin"]},
        ),
    )

    fieldsets = (
        (
            "Details",
            {
                "fields": [
                    "id",
                    "uuid",
                    "email",
                    "name",
                    "bio",
                ]
            },
        ),
        (
            "Access",
            {
                "fields": [
                    "is_active",
                    "is_admin",
                    "password",
                ]
            },
        ),
        ("Dates", {"fields": ["created_at", "updated_at"]}),
    )
