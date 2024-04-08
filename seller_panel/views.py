from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from seller_panel.models import Products, Category
from seller_panel.serializer import ProductsSerializer, CategorySerializer, SellerDashboardSerializer
from testing_app.models import Sales_product


# Create your views here.


class CategoryView(APIView):
    @staticmethod
    def get(request):
        user = Category.objects.all()
        serializer = CategorySerializer(user, many=True)
        return Response(serializer.data, 200)

    @staticmethod
    def post(request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                "status": "Product save successfully",
                "data": serializer.data,
                "status_code": 200
            })
        return Response({
            "status": "something data wrong or missing",
            "data": serializer.errors,
            "status_code": 400
        })


class ProductsView(APIView):
    @staticmethod
    def get(request):
        user = Products.objects.all()
        serializer = ProductsSerializer(user, many=True)
        return Response(serializer.data, 200)


class ProductsViewId(APIView):
    """
    Retrieve Product instance.
    """

    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductsSerializer(snippet)
        return Response(serializer.data)


class SellerDashboardView(APIView):
    @staticmethod
    def get(request):
        user = Products.objects.all()
        serializer = SellerDashboardSerializer(user, many=True)
        return Response(serializer.data, 200)

    @staticmethod
    def post(request):
        serializer = SellerDashboardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                "status": "Product save successfully",
                "data": serializer.data,
                "status_code": 200
            })
        return Response({
            "status": "something data wrong or missing",
            "data": serializer.errors,
            "status_code": 400
        })
