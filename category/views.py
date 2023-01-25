from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from rest_framework import generics

from .models import Category
from rest_framework import  viewsets
from .serializers import CategorySerializer


class CategoryRetrieveView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




