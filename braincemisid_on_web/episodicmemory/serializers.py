from rest_framework import serializers
from .classes import EpisodicMemoryClass

class EpisodicMemorySerializer(serializers.Serializer):
    _has_knowledge = serializers.BooleanField()
    _knowledge = serializers.JSONField(default='')
    group_number= serializers.IntegerField()

    def create(self, validated_data):
        return EpisodicMemoryClass(**validated_data)
    
    def update(self, instance, validated_data):
        instance._has_knowledge = validated_data.get('_has_knowledge', instance._has_knowledge)
        instance._knowledge = validated_data.get('_knowledge', instance._knowledge)
        instance.group_number = validated_data.get('group_number', instance.group_number)
        return instance