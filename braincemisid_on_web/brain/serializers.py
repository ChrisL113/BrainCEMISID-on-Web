from rest_framework import serializers

from .classes import BrainOutputClass
from .models import brain

############################################## kernel ###########################################

class BrainOutputSerializer(serializers.Serializer):
    h_knowledge = serializers.JSONField(default='')
    s_knowledge = serializers.JSONField(default='')
    biology =  serializers.FloatField(min_value=0,max_value=1) 
    culture =  serializers.FloatField(min_value=0,max_value=1)
    feelings = serializers.FloatField(min_value=0,max_value=1)
    desired_biology =  serializers.FloatField(min_value=0,max_value=1) 
    desired_culture =  serializers.FloatField(min_value=0,max_value=1)
    desired_feelings = serializers.FloatField(min_value=0,max_value=1)
    state= serializers.CharField(max_length=100)

    def create(self, validated_data):
        return BrainOutputClass(**validated_data)

    def update(self, instance, validated_data):
        instance.h_knowledge = validated_data.get('h_knowledge',instance.h_knowledge)
        instance.s_knowledge = validated_data.get('s_knowledge', instance.s_knowledge)
        instance.biology =  validated_data.get('biology',instance.biology)
        instance.culture = validated_data.get('culture',instance.culture)
        instance.feelings = validated_data.get('feelings',instance.feelings)
        instance.desired_biology =  validated_data.get('desired_biology',instance.desired_biology)
        instance.desired_culture = validated_data.get('desired_culture',instance.desired_culture)
        instance.desired_feelings = validated_data.get('desired_feelings',instance.desired_feelings)
        instance.state= validated_data.get('state',instance.state)


class ProjectSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model= brain
        fields = ['id', 'name', 'internal_state','desired_state']

""" 
class testSerializer(serializers.Serializer):
    test = serializers.JSONField(default='')
    
    def create(self, validated_data):
        return testClass(**validated_data)
    
    def update(self, instance, validated_data):
        instance.test = validated_data.get('test', instance.test)
        return instance """