from rest_framework import serializers
from images_settings.models import ImageSettings

class ImagesSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model= ImageSettings
        fields = '__all__'