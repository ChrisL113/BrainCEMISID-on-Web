from rest_framework import  viewsets, permissions
from .serializers import RelNetworkSerializer
from .classes import RelNetworkClass
from rest_framework.response import Response

#from django.contrib.auth.models import User
#from django.db import connection
import pickle
#import json


class RelNetworkViewSet(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = RelNetworkSerializer
    def list(self, request):
        
        project_id=self.request.query_params.get('project_id')
        pickled_data=self.request.user.brain.get(pk=project_id).rnb
        
        rel_network=[]
        if pickled_data!=None:
            aux = pickle.loads(pickled_data)
            for i in aux.neuron_list:
                if i._knowledge!=None:
                    rel_network.append(RelNetworkClass(i._hit,i._knowledge,i._has_knowledge))
            serializer = RelNetworkSerializer(instance=rel_network, many=True)
        
            return Response(serializer.data)
        else:
            return Response({'message':'NOT FOUND'})
