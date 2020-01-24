from rest_framework import serializers
from .classes import EpisodicMemoryClass

class EpisodicMemorySerializer(serializers.Serializer):
    episode= serializers.ListField(child=serializers.JSONField(default=''))


    def create(self, validated_data):
        return EpisodicMemoryClass(**validated_data)
    
    def update(self, instance, validated_data):
        instance.episode = validated_data.get('episode', instance.episode)
        
        return instance