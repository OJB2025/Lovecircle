from rest_framework import viewsets

from .models import Swipe
from .serializers import SwipeSerializer


class SwipeViewSet(viewsets.ModelViewSet):
    queryset = Swipe.objects.all()
    serializer_class = SwipeSerializer
