from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from contact.serializer import ContactSerializer


# Create your views here.


class ContactView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
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
