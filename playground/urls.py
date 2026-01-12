# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet
from . import views  # for other non-API views like index

# Create a single router and register the viewsets
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', views.index, name='index'),  # your non-API view
    path('api/', include(router.urls)),   # API routes
]
