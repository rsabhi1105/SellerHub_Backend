from rest_framework import serializers

from customer_panel.models import UserProfile, Cart, Rating, Vendor


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "name", "mobile_no", "email", "address", "pincode",
            "near_landmark", "user_image",
        ]


class CartSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(read_only=True, source="product.product_name")
    product_image = serializers.CharField(read_only=True, source="product.image")
    product_brand = serializers.CharField(read_only=True, source="product.brand")
    product_price = serializers.CharField(read_only=True, source="product.price")

    class Meta:
        model = Cart
        fields = [
            "user", "product", "product_name", "product_image", "product_brand",
            "product_price", "quantity", "created_at", "updated_at",

        ]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = [
            "user", "product", "rating", "created_at", "updated_at"
        ]


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            "user_name", "email", "company_name", "mobile_no", "address",
            "pincode", "near_landmark", "gst", "brand_name", "bank_name", "account_no",
            "ifc_code", "created_at", "updated_at",
        ]
