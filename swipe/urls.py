from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SwipeViewSet

router = DefaultRouter()
router.register(r'swipes', SwipeViewSet, basename='swipe')

urlpatterns = [
    path('', include(router.urls)),
]
