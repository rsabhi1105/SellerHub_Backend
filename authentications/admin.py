from django.contrib import admin

from authentications.models import User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "phone_number",
                    "is_vendor", "created_at", "updated_at"]
