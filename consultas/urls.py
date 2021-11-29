#Rest Framework
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
#Django
from django.urls import path
#Views
from .views import CiudadAPIView

# router = DefaultRouter()
# router.register('api/ciudad', CiudadAPIView)

urlpatterns = [
    path('api/ciudades/<str:ciudad>/', CiudadAPIView.as_view(), name="ciudades"),
]
