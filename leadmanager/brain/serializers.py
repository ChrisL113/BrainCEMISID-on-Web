from rest_framework import serializers
from .models import Projects

from .classes import StatusClass, NeuronNetworkClass, KernelClass,testClass

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class KernelSerializer(serializers.Serializer):
    status = serializers.JSONField(default='')
    sight_network = serializers.JSONField(default='')
    hearing_network = serializers.JSONField(default='')

    def create(self, validated_data):
        return kernelClass(**validated_data)
    
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.sight_network = validated_data.get('sight_network',instance.sight_network)
        instance.hearing_network = validated_data.get('hearing_network',instance.hearing_network)
        return instance

############################################## kernel ###########################################

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

class testSerializer(serializers.Serializer):
    test = serializers.JSONField(default='')
    
    def create(self, validated_data):
        return testClass(**validated_data)
    
    def update(self, instance, validated_data):
        instance.test = validated_data.get('test', instance.test)
        return instance

class NeuronNetworkSerializer(serializers.Serializer):
    _has_knowledge = serializers.BooleanField()
    _radius = serializers.FloatField()
    _degraded = serializers.BooleanField()
    _knowledge = serializers.JSONField(default='')

    def create(self, validated_data):
        return NeuronNetworkClass(**validated_data)
    
    def update(self, instance, validated_data):
        instance._has_knowledge = validated_data.get('_has_knowledge', instance._has_knowledge)
        instance._radius = validated_data.get('_radius', instance._radius)
        instance._degraded = validated_data.get('_degraded', instance._degraded)
        instance._knowledge = validated_data.get('_knowledge', instance._knowledge)
        return instance
