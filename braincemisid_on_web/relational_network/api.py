from rest_framework import  viewsets, permissions
from .serializers import RelNetworkSerializer
from .classes import RelNetworkClass
from rest_framework.response import Response
from brain.models import *
import json


class RelNetworkViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = RelNetworkSerializer
    def list(self, request):
        
        project_id=self.request.query_params.get('project_id')
        if project_id==None:
            return Response({'message':'There is not project, please provide the id :)'})
        #rnb_data=rnb.objects.filter(brain_rnb__pk=project_id)
        neurons_from_db=RnbNeuron.objects.filter(rnb__brain_rnb__pk=project_id, has_knowledge=True).order_by('id')
        #pickled_data=self.request.user.brain.get(pk=project_id).rnb
        
        rel_network=[]
        if neurons_from_db!=None:
            for i in neurons_from_db.values():
                if i['has_knowledge']==True:
                    aux=json.loads(i['knowledge'])
                    rel_network.append(RelNetworkClass(i['hit'],aux,i['has_knowledge']))
            serializer = RelNetworkSerializer(instance=rel_network, many=True)
        
            return Response(serializer.data)
        else:
            return Response({'message':'NOT FOUND'})
