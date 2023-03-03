from django.shortcuts import render
from rest_framework import generics

from apis.serializers import BookSerializers
from books.models import Book


# Create your views here.

class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
