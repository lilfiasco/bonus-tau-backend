from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CardViewSet


router = DefaultRouter()
router.register('cards', CardViewSet, basename='cards')

urlpatterns = [
    path('', include(router.urls)),
]