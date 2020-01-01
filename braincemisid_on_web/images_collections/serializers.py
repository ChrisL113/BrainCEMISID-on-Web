from rest_framework import serializers
from images_collections.models import ImagesFromNeuron

class ImagesFromNeuronSerializer(serializers.ModelSerializer):
    class Meta:
        model= ImagesFromNeuron
        fields = '__all__'