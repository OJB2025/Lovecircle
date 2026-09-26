from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import PhotoViewSet

router = SimpleRouter()
router.register(r'photos', PhotoViewSet, basename='photo')

urlpatterns = [
    path('', include(router.urls)),
]
