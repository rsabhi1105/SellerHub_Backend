from django.db import models
from django.template.defaultfilters import truncatechars

from authentications.models import User


# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    product_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/products/", null=True)
    brand = models.CharField(max_length=50, default="no brand")
    price = models.IntegerField()
    discount = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    sales = models.IntegerField(default=0)
    revenue = models.IntegerField(default=0)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 15)

    def __str__(self):
        return self.product_name
