from django.contrib import admin

from seller_panel.models import Products, Category


# Register your models here.
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ["category"]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    readonly_fields = ["sales", "revenue"]

    list_display = ["id", "user", "product_name", "category", "image","brand",
                    "short_description", "price", "discount",
                    "stock", "sales", "revenue",
                    "created_at", "updated_at",
                    ]
