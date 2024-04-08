from django.db import models
from authentications.models import User
from seller_panel.models import Products


# Create your models here.
class UserProfile(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=255)
    pincode = models.IntegerField()
    near_landmark = models.CharField(max_length=255)
    user_image = models.ImageField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.product)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="rating")
    rating = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.product)


class Vendor(models.Model):
    # vendor and company contact.....
    user_name = models.CharField(max_length=255)
    email = models.EmailField()
    company_name = models.CharField(max_length=255)
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=255)
    pincode = models.IntegerField()
    near_landmark = models.CharField(max_length=255)
    # company legal overview.....
    gst = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)
    # banking_details........
    bank_name = models.CharField(max_length=255)
    account_no = models.IntegerField()
    ifc_code = models.CharField(max_length=50)
    # updated details............
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def short_address(self):
        return self.address[:15]

    def __str__(self):
        return self.company_name
