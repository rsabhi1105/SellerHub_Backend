from django.contrib import admin

from customer_panel.models import UserProfile, Cart, Rating, Vendor


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "mobile_no", "email", "address", "pincode",
                    "near_landmark", "user_image",
                    ]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "quantity", "created_at", "updated_at"]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "rating", "created_at", "updated_at"]


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = [
        "user_name", "email", "company_name", "mobile_no", "address",
        "pincode", "near_landmark", "gst", "brand_name", "bank_name", "account_no",
        "ifc_code", "created_at", "updated_at",

    ]
