"""
URL configuration for sammissishops project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls'))
]
path('api/', include('playground.urls')),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('playground.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    # include the playground app
    path('playground/', include('playground.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('playground.urls')),  # includes the API
]

urlpatterns = [
    path('admin/', admin.site.urls),
    # include playground routes
    path('playground/', include('playground.urls')),
]
