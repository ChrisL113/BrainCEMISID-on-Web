from rest_framework import serializers
from brain.models import RbfNeuronHearing

class NeuronHearingSerializer(serializers.ModelSerializer):
    class Meta:
        model= RbfNeuronHearing
        fields = '__all__'