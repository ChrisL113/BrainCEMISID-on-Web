from rest_framework import serializers
from .classes import EpisodicMemoryClass

class EpisodicMemorySerializer(serializers.Serializer):
    group_list= serializers.ListField(child=serializers.JSONField(default=''))
    _clack= serializers.BooleanField()
    _recognized_indexes=serializers.JSONField(default='')

    def create(self, validated_data):
        return EpisodicMemoryClass(**validated_data)
    
    def update(self, instance, validated_data):
        instance.group_list = validated_data.get('group_list', instance.group_list)
        instance._clack = validated_data.get('_clack', instance._clack)
        instance._recognized_indexes = validated_data.get('_recognized_indexes', instance._recognized_indexes)
        return instance