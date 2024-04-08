from django.contrib import admin

from contact.models import Contact


# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message", "created_at", "updated_at"]
