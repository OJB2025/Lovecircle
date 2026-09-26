from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import PaymentViewSet

router = SimpleRouter()
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]
