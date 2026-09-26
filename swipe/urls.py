from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import SwipeViewSet

router = SimpleRouter()
router.register(r'swipes', SwipeViewSet, basename='swipe')

urlpatterns = [
    path('', include(router.urls)),
]
