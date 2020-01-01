from rest_framework import serializers

from .classes import StatusClass

class StatusSerializer(serializers.Serializer):
    biology = serializers.FloatField(min_value=0,max_value=1)
    culture = serializers.FloatField(min_value=0,max_value=1)
    feelings = serializers.FloatField(min_value=0,max_value=1)

    def create(self, validated_data):
        return StatusClass(**validated_data)
    
    def update(self, instance, validated_data):
        instance.biology = validated_data.get('biology', instance.biology)
        instance.culture = validated_data.get('cultural',instance.culture)
        instance.feelings = validated_data.get('feelings',instance.feelings)
        return instance