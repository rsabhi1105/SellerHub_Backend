from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from authentications.models import User
from customer_panel.models import UserProfile, Cart, Rating, Vendor
from customer_panel.serializer import UserProfileSerializer, CartSerializer, RatingSerializer, VendorSerializer


# Create your views here.
class UserProfileView(APIView):
    @staticmethod
    def get(request):
        user = UserProfile.objects.all()
        serializer = UserProfileSerializer(user, many=True)
        return Response(serializer.data, 200)

    @staticmethod
    def post(request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                "status": "Profile save successfully",
                "user": serializer.data,
                "status_code": 200
            })
        return Response({
            "status": "Some data missing or wrong",
            "error": serializer.errors,
            "status_code": 400

        })


class CartView(APIView):
    @staticmethod
    def get(request):
        user = Cart.objects.all()
        serializer = CartSerializer(user, many=True)
        return Response(serializer.data, 200)

    @staticmethod
    def post(request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                "status": "ok",
                "data": serializer.data,
                "status_code": 200
            })
        return Response({
            "status": "something data wrong or missing",
            "data": serializer.errors,
            "status_code": 400
        })


class RatingView(APIView):
    @staticmethod
    def get(request):
        user = Rating.objects.all()
        serializer = RatingSerializer(user, many=True)
        return Response(serializer.data, 200)

    @staticmethod
    def post(request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                "status": "Rating save successfully",
                "data": serializer.data,
                "status_code": 200
            })
        return Response({
            "status": "something data wrong or missing",
            "data": serializer.errors,
            "status_code": 400
        })


class VendorView(APIView):
    @staticmethod
    def get(request):
        user = Vendor.objects.all()
        serializer = VendorSerializer(user, many=True)
        return Response(serializer.data, 200)

    @staticmethod
    def post(request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data["email"]
            if not Vendor.objects.filter(email=email).exists():
                try:
                    user = User.objects.get(email=email)
                    user.is_vendor = True
                    user.save()
                except ObjectDoesNotExist:
                    return Response({
                        "status": "you are already a vendor.",
                        "data": serializer.errors,
                        "status_code": 400
                    })

                serializer.save()
                return Response({
                    "status": "Vendor saved successfully",
                    "data": serializer.data,
                    "status_code": 200
                })
            else:
                return Response({
                    "status": "Vendor already exists. Please try with your account.",
                    "data": serializer.errors,
                    "status_code": 400
                })
