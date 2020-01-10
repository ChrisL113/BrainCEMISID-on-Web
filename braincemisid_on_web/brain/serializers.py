from rest_framework import serializers

from .classes import BrainOutputClass
from .models import brain

############################################## kernel ###########################################

class BrainOutputSerializer(serializers.Serializer):
    h_pattern = serializers.JSONField(default='')
    hearing_class=serializers.CharField(max_length=200)
    s_pattern = serializers.JSONField(default='')
    neuron_number = serializers.IntegerField()
    biology =  serializers.FloatField(min_value=0,max_value=1) 
    culture =  serializers.FloatField(min_value=0,max_value=1)
    feelings = serializers.FloatField(min_value=0,max_value=1)
    state= serializers.CharField(max_length=100)

    def create(self, validated_data):
        return BrainOutputClass(**validated_data)

    def update(self, instance, validated_data):
        instance.h_pattern = validated_data.get('h_pattern',instance.h_pattern)
        instance.hearing_class = validated_data.get('hearing_class', instance.hearing_class)
        instance.s_pattern = validated_data.get('s_pattern',instance.s_pattern)
        instance.neuron_number = validated_data.get('neuron_number',instance.neuron_number)
        instance.biology =  validated_data.get('biology',instance.biology)
        instance.culture = validated_data.get('culture',instance.culture)
        instance.feelings = validated_data.get('feelings',instance.feelings)
        instance.state= validated_data.get('state',instance.state)


class ProjectSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model= brain
        fields = ['id', 'name', 'internal_state']

""" 
class testSerializer(serializers.Serializer):
    test = serializers.JSONField(default='')
    
    def create(self, validated_data):
        return testClass(**validated_data)
    
    def update(self, instance, validated_data):
        instance.test = validated_data.get('test', instance.test)
        return instance """