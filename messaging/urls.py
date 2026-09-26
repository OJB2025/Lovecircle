from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import ConversationViewSet, MessageViewSet

router = SimpleRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
]
