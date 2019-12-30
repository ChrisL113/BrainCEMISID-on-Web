from rest_framework import  viewsets, permissions
from .serializers import  NeuronSightSerializer#,NeuronNetworkSerializer
#from .classes import NeuronNetworkClass
from rest_framework.response import Response

#from django.contrib.auth.models import User
#from django.db import connection
#import pickle
#import json

from brain.models import RbfNeuronSight

# class SightNetworkViewSet(viewsets.ViewSet):
#     #permission_classes = [
#     #    permissions.IsAuthenticated
#     #]
#     serializer_class = NeuronNetworkSerializer
#     def list(self, request):
#         if "user_id" in request.data and "project_id" in request.data:
#             user_id=request.data['user_id']
#             project_id=request.data['project_id']
#             with connection.cursor() as cur:
#                 cur.execute('SELECT snb_s FROM brain_brain WHERE user_id=%s AND id=%s',[user_id,project_id])
#                 pickled_data = cur.fetchone()
            
#             sight_network=[]
#             if pickled_data!=None:
#                 aux = pickle.loads(pickled_data[0])
#                 for i in aux.neuron_list:
#                     if i._knowledge!=None:
#                         sight_network.append(NeuronNetworkClass(i._has_knowledge,i._radius,i._degraded,json.dumps(i._knowledge.__dict__)))
#                     else:
#                         sight_network.append(NeuronNetworkClass(i._has_knowledge,i._radius,i._degraded,None))
#                 serializer = NeuronNetworkSerializer(instance=sight_network, many=True)
#                 return Response(serializer.data)
#             else:
#                 return Response({'message':'NOT FOUND'})
#         else:
#             return Response({'message':'NOT SUFFICIENT OR ANY DATA SUPPLIED PLEASE, PASS THE ARGUMENTS project_id AND user_id'})

class SightNeuronsViewSet(viewsets.ViewSet):
    #permission_classes = [
    #    permissions.IsAuthenticated
    #]
    
    
    def list(self, request):
        
        if  "project_id" in request.data:
            
            project_id=request.data['project_id']
            try:
                query=RbfNeuronSight.objects.filter(snb_sight__brain_s__pk=project_id, has_knowledge=True)
                #print(query.values())
                serializer = NeuronSightSerializer(instance=query, many=True)
            except:
                return Response({'message':'There was an error, please, check the project_id'})
        
            return Response(serializer.data)
        #     sight_network=[]
        #     if pickled_data!=None:
        #         aux = pickle.loads(pickled_data[0])
        #         for i in aux.neuron_list:
        #             if i._knowledge!=None:
        #                 sight_network.append(NeuronNetworkClass(i._has_knowledge,i._radius,i._degraded,json.dumps(i._knowledge.__dict__)))
        #             else:
        #                 sight_network.append(NeuronNetworkClass(i._has_knowledge,i._radius,i._degraded,None))
        #         serializer = NeuronNetworkSerializer(instance=sight_network, many=True)
        #         return Response(serializer.data)
        #     else:
        #         return Response({'message':'NOT FOUND'})
        # else:
        #     