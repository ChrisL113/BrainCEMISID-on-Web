from rest_framework import serializers
from .models import Projects

from .classes import StatusClass,NeuronNetworkClass,BrainOutputClass

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

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

class BrainOutputSerializer(serializers.Serializer):
    h_has_knowledge = serializers.BooleanField()
    h_radius = serializers.FloatField()
    h_degraded = serializers.BooleanField()
    h_knowledge = serializers.JSONField(default='')
    s_has_knowledge = serializers.BooleanField()
    s_radius = serializers.FloatField()
    s_degraded = serializers.BooleanField()
    s_knowledge = serializers.JSONField(default='')
    biology =  serializers.FloatField(min_value=0,max_value=1) 
    culture =  serializers.FloatField(min_value=0,max_value=1)
    feelings = serializers.FloatField(min_value=0,max_value=1)
    state= serializers.CharField(max_length=100)

    def create(self, validated_data):
        return BrainOutputClass(**validated_data)

    def update(self, instance, validated_data):
        instance.h_has_knowledge = validated_data.get('h_has_knowledge',instance.h_has_knowledge) 
        instance.h_radius = validated_data.get('h_radius',instance.h_radius)
        instance.h_degraded = validated_data.get('h_degraded',instance.h_degraded)
        instance.h_knowledge = validated_data.get('h_knowledge',instance.h_knowledge)
        instance.s_has_knowledge = validated_data.get('s_has_knowledge',instance.s_has_knowledge)
        instance.s_radius = validated_data.get('s_radius',instance.s_radius)
        instance.s_degraded = validated_data.get('s_degraded',instance.s_degraded)
        instance.s_knowledge = validated_data.get('s_knowledge',instance.s_knowledge)
        instance.biology =  validated_data.get('biology',instance.biology)
        instance.culture = validated_data.get('culture',instance.culture)
        instance.feelings = validated_data.get('feelings',instance.feelings)
        instance.state= validated_data.get('state',instance.state)



""" 
class testSerializer(serializers.Serializer):
    test = serializers.JSONField(default='')
    
    def create(self, validated_data):
        return testClass(**validated_data)
    
    def update(self, instance, validated_data):
        instance.test = validated_data.get('test', instance.test)
        return instance """