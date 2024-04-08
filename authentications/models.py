from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(unique=True)
    is_vendor = models.BooleanField(default=False, null=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number"]

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
            super().save(*args, **kwargs)

    def __str__(self):
        return self.email
