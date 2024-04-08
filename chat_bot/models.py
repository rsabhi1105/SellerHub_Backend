from django.db import models

from authentications.models import User


# Create your models here.


class ChatBot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vector_db = models.BooleanField(default=False)
    documents = models.FileField(upload_to="documents/")
    user_chat = models.CharField(max_length=255)
    response_chat = models.CharField(max_length=255)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.email
