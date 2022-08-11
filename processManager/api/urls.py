from django.urls import path, include
from rest_framework import routers
from .views import ProcessViewSet

router = routers.DefaultRouter()
router.register('', ProcessViewSet, basename='Process')
