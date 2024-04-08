from django.urls import path
from seller_panel.views import CategoryView, ProductsView, SellerDashboardView, ProductsViewId

urlpatterns = [
    path("category/", CategoryView.as_view()),
    path("product/", ProductsView.as_view()),
    path("product/<int:pk>/", ProductsViewId.as_view()),
    path("seller_dashboard/", SellerDashboardView.as_view()),
]
