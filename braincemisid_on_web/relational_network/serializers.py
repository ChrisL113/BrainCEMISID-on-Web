from rest_framework import serializers

from .classes import RelNetworkClass

class BrainOutputSerializer(serializers.Serializer):
    _weight= serializers.FloatField() 
    _h_id= serializers.IntegerField()
    _s_id= serializers.IntegerField()
    _has_knowledge= serializers.BooleanField()
    _hit= serializers.BooleanField()


    def create(self, validated_data):
        return RelNetworkClass(**validated_data)

    def update(self, instance, validated_data):
        instance._has_knowledge=validated_data.get('_has_knowledge',instance._has_knowledge) 
        instance._hit=validated_data.get('_hit',instance._hit)
        instance._h_id= validated_data.get('_h_id',instance._h_id)
        instance._s_id=validated_data.get('_s_id',instance._s_id)
        instance._weight=validated_data.get('_weight',instance._weight)
        instance.h_pattern = validated_data.get('h_pattern',instance.h_pattern)
