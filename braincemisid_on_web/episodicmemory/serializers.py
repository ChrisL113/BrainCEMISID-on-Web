from rest_framework import serializers
from .classes import EpisodicMemoryClass

class EpisodicMemorySerializer(serializers.Serializer):
    group_01 = serializers.JSONField(default='')
    group_02 = serializers.JSONField(default='')
    index_bip= serializers.IntegerField()

    def create(self, validated_data):
        return EpisodicMemoryClass(**validated_data)
    
    def update(self, instance, validated_data):
        instance.group_01 = validated_data.get('group_01', instance.group_01)
        instance.group_02 = validated_data.get('group_02', instance.group_02)
        instance.index_bip = validated_data.get('index_bip', instance.index_bip)
        return instance