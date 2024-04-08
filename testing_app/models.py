from django.db import models

from authentications.models import User
from seller_panel.models import Products


# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Song(models.Model):
    song_name = models.CharField(max_length=255)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="song")

    def __str__(self):
        return self.song_name


class Sales_product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_order = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="sales_p")
    quantity = models.IntegerField(default=1)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.product_order)
