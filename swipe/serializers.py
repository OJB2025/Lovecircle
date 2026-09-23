from rest_framework import serializers

from .models import Swipe


class SwipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swipe
        fields = ['id', 'swiper', 'swipee', 'direction', 'created_at']
        read_only_fields = ['id', 'created_at']
