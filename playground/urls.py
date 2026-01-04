from django.urls import path, include
from . import views  # make sure views.py exists
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = router.urls

# playground/urls.py

urlpatterns = [
    path('', views.index, name='index'),  # this will match /playground/
]

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('api/', include(router.urls)),
]

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
