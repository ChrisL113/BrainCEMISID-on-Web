from rest_framework import  viewsets, permissions
from .serializers import RelNetworkSerializer
from .classes import RelNetworkClass
from rest_framework.response import Response

import pickle


class RelNetworkViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = RelNetworkSerializer
    def list(self, request):
        
        project_id=self.request.query_params.get('project_id')
        if project_id==None:
            return Response({'message':'There is not project, please provide the id :)'})
            
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
