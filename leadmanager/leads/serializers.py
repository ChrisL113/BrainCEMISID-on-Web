from rest_framework import serializers
from leads.models import Lead

from .classes import brain_state, SightNetworkClass, HearingNetworkClass,testClass

# Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class SignalSerializer(serializers.Serializer):
    signal_wihout_ouput = serializers.CharField(max_length=200)
    signal_with_ouput = serializers.CharField(max_length=200)
    working_domain = serializers.CharField(max_length=200)

class PayLoadSerializer(serializers.Serializer):
    hearing_class = serializers.CharField(max_length=200)
    hearing_pattern = serializers.ListField(
         child=serializers.IntegerField(max_value=64)
    ) 
    sight_pattern = serializers.ListField(
         child=serializers.IntegerField(max_value=64)
    )

class BrainStateSerializer(serializers.Serializer):
    biology = serializers.FloatField(min_value=0,max_value=1)
    cultural = serializers.FloatField(min_value=0,max_value=1)
    feelings = serializers.FloatField(min_value=0,max_value=1)

    def create(self, validated_data):
        return brain_state(**validated_data)
    
    def update(self, instance, validated_data):
        instance.biology = validated_data.get('biology', instance.biology)
        instance.cultural = validated_data.get('cultural',instance.cultural)
        instance.feelings = validated_data.get('feelings',instance.feelings)
        return instance

class testSerializer(serializers.Serializer):
    test = serializers.JSONField(default='')
    

    def create(self, validated_data):
        return testClass(**validated_data)
    
    def update(self, instance, validated_data):
        instance.test = validated_data.get('test', instance.test)
        return instance

class SightNetworkSerializer(serializers.Serializer):
    _has_knowledge = serializers.BooleanField()
    _radius = serializers.FloatField()
    _degraded = serializers.BooleanField()
    _knowledge = serializers.JSONField(default='')

    def create(self, validated_data):
        return SightNetworkClass(**validated_data)
    
    def update(self, instance, validated_data):
        instance._has_knowledge = validated_data.get('_has_knowledge', instance._has_knowledge)
        instance._radius = validated_data.get('_radius', instance._radius)
        instance._degraded = validated_data.get('_degraded', instance._degraded)
        instance._knowledge = validated_data.get('_knowledge', instance._knowledge)
        return instance

class HearingNetworkSerializer(serializers.Serializer):
    _has_knowledge = serializers.BooleanField()
    _radius = serializers.FloatField()
    _degraded = serializers.BooleanField()
    _knowledge = serializers.JSONField(default='')

    def create(self, validated_data):
        return HearingNetworkClass(**validated_data)
    
    def update(self, instance, validated_data):
        instance._has_knowledge = validated_data.get('_has_knowledge', instance._has_knowledge)
        instance._radius = validated_data.get('_radius', instance._radius)
        instance._degraded = validated_data.get('_degraded', instance._degraded)
        instance._knowledge = validated_data.get('_knowledge', instance._knowledge)
        return instance

class Serializer(serializers.Serializer):
    pass
