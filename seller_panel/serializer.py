from rest_framework import serializers

import testing_app
from customer_panel.serializer import RatingSerializer
from seller_panel.models import Products, Category
from testing_app.models import Sales_product


class ProductsSerializer(serializers.ModelSerializer):
    rating = RatingSerializer(many=True, read_only=True)
    category = serializers.CharField(source="category.category")

    class Meta:
        model = Products
        fields = [
            "id", "user", "product_name", "category", "brand", "image", "description", "price",
            "discount", "rating", "created_at", "updated_at"]


class CategorySerializer(serializers.ModelSerializer):
    product = ProductsSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "category", "product"]


class SellerDashboardSerializer(serializers.ModelSerializer):
    rating = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = [
            "user", "category", "product_name", "image", "price", "discount", "description", "rating",
            "stock", "sales", "revenue", "created_at", "updated_at",
        ]
