from.models import Product
from .serializer import ProductSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
class ProductListcreate(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	filter_backends =[OrderingFilter,DjangoFilterBackend]
	ordering_fields = ["price"]
	filterset_fields = ['created_by']
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class Listproduct(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	filter_backends =[OrderingFilter,DjangoFilterBackend]
	ordering_fields = ["price"]
	filterset_fields = ['created_by']

