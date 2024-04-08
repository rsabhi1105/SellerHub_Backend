from django.shortcuts import render
from rest_framework import generics

from testing_app.models import Singer, Song, Sales_product
from testing_app.serializer import SingerSerializer, SongSerializer, SalesSerializer


# Create your views here.

class SingerView(generics.ListCreateAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SalesView(generics.ListCreateAPIView):
    queryset = Sales_product.objects.all()
    serializer_class = SalesSerializer
