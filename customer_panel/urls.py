from django.urls import path

from customer_panel.views import UserProfileView, CartView, RatingView, VendorView

urlpatterns = [
    path("userprofile/", UserProfileView.as_view()),
    path("cart/", CartView.as_view()),
    path("rating/", RatingView.as_view()),
    path("vendor/", VendorView.as_view()),
]
