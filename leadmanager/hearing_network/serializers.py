from rest_framework import serializers
#from .models import RbfNeuron

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
""" 
class NeuronNetworkProto(serializers.ModelSerializer):
    class Meta:
        model = RbfNeuron
        fields = '__all__'
 """