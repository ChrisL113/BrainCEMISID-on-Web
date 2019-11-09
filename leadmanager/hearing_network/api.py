from rest_framework import  viewsets, permissions
from .serializers import  NeuronNetworkSerializer,NeuronNetworkProto
from .classes import NeuronNetworkClass
from rest_framework.response import Response
from django.contrib.auth.models import User

from django.db import connection
import pickle
import json

class SightNetProto(viewsets.ViewSet):
    #permission_classes = [
    #    permissions.IsAuthenticated
    #]
    serializer_class = NeuronNetworkProto
    def get_queryset(self):
        return self.request.user.brains.snb_s.rbf_neurons.all()
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class HearingNetworkViewSet(viewsets.ViewSet):
    #permission_classes = [
    #    permissions.IsAuthenticated
    #]
    serializer_class = NeuronNetworkSerializer
    def list(self, request):
        if "user_id" in request.data and "project_id" in request.data:
            user_id=request.data['user_id']
            project_id=request.data['project_id']
            with connection.cursor() as cur:
                cur.execute('SELECT snb_h FROM brain WHERE user_id=%s AND id=%s',[user_id,project_id])
                pickled_data = cur.fetchone()
            hearing_network=[]
            if pickled_data!=None:
                aux = pickle.loads(pickled_data[0])
                for i in aux.neuron_list:
                    if i._knowledge!=None:
                        hearing_network.append(NeuronNetworkClass(i._has_knowledge,i._radius,i._degraded,json.dumps(i._knowledge.__dict__)))
                    else:
                        hearing_network.append(NeuronNetworkClass(i._has_knowledge,i._radius,i._degraded,None))
                serializer = NeuronNetworkSerializer(instance=hearing_network, many=True)
                return Response(serializer.data)
            else:
                return Response({'message':'NOT FOUND'})
        else:
            return Response({'message':'NOT SUFFICIENT OR ANY DATA SUPPLIED PLEASE, PASS THE ARGUMENTS project_id AND user_id'})

