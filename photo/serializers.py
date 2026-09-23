from rest_framework import serializers

from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'user', 'image', 'caption', 'is_profile', 'created_at']
        read_only_fields = ['id', 'created_at']
