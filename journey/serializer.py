from rest_framework import serializers
from .models import DestinationImages,Gallery

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'image']

class DestModel(serializers.ModelSerializer):
    gallery = GallerySerializer(many=True, read_only=True)
    class Meta:
        model = DestinationImages
        fields = '__all__'
