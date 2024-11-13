from django.urls import path, include
from rest_framework import routers

from movies.views import CategoryViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'movie', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]