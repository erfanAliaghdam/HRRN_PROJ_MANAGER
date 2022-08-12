from django.urls import path, include
from .api.urls import router



urlpatterns = [
    path('process', include(router.urls))
]
