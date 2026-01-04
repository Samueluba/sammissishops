# playground/views.py

from django.http import HttpResponse
from rest_framework import viewsets, permissions, filters
# Correct import for FilterSet
from django_filters import rest_framework as django_filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly


# Simple index view
def index(request):
    return HttpResponse("Hello from playground!")


# -------------------------------
# Filter class for Products
# -------------------------------
class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(
        field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(
        field_name="price", lookup_expr='lte')
    in_stock = django_filters.BooleanFilter(method='filter_in_stock')

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price', 'in_stock']

    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock_quantity__gt=0)
        return queryset


# -------------------------------
# Product ViewSet
# -------------------------------
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'category__name']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# -------------------------------
# Category ViewSet
# -------------------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
