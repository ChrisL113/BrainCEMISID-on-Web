from rest_framework import  viewsets, permissions,mixins
from .serializers import  NeuronNetworkSerializer,ProjectSerializer, KernelSerializer,StatusSerializer,testSerializer
from .classes import NeuronNetworkClass # classes
from rest_framework.response import Response

from django.db import connection
import pickle
import sys
import json

#################################### kernel################################################
sys.path.append('D:\Desktop\BrainCEMISID on Web\leadmanager\kernel')
from kernel_braincemisid import KernelBrainCemisid 

#Project Viewset
class ProjectViewset(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.request.user.projects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class KernelViewSet(viewsets.ViewSet):
    kernel=None
    #serializer_class=KernelSerializer
    def create(self,request):
        if "user_id" in request.data and "project_id" in request.data and "exists" in request.data:
            try:
                kernel=KernelBrainCemisid(request.data['user_id'],request.data['project_id'],request.data['exists'])
            except:    
                return Response({'message':'NOT FOUND'})
            
            return Response({'message':'BRAIN IS ALREADY LOADED'})
        else:    
            return Response({'message':'NOT SUFFICIENT OR ANY DATA SUPPLIED, PLEASE PASS THE ARGUMENTS project_id AND user_id'})
    pass

class InternalStatusViewSet(viewsets.ViewSet):
    #permission_classes = [
    #    permissions.IsAuthenticated
    #]
    serializer_class = StatusSerializer
    def list(self, request):
        if "user_id" in request.data and "project_id" in request.data:
            user_id=request.data['user_id']
            project_id=request.data['project_id']
            cur=connection.cursor()
            cur.execute('SELECT internal_state FROM brain WHERE user_id=%s AND id=%s',[user_id,project_id])
            pickled_data = cur.fetchone()
            if pickled_data!=None:
                int_status=pickle.loads(pickled_data[0])
                serializer = StatusSerializer(int_status.__dict__)
                return Response(serializer.data)
            else:
                return Response({'message':'NOT FOUND'})
        else:
            return Response({'message':'NOT SUFFICIENT OR ANY DATA SUPPLIED, PLEASE PASS THE ARGUMENTS project_id AND user_id'})

class DesiredStatusViewSet(viewsets.ViewSet):
    #permission_classes = [
    #    permissions.IsAuthenticated
    #]
    serializer_class = StatusSerializer
    def list(self, request):
        if "user_id" in request.data and "project_id" in request.data:
            user_id=request.data['user_id']
            project_id=request.data['project_id']
            cur=connection.cursor()
            cur.execute('SELECT desired_state FROM brain WHERE user_id=%s AND id=%s',[user_id,project_id])
            pickled_data = cur.fetchone()
            if pickled_data!=None:
                int_status=pickle.loads(pickled_data[0])
                serializer = StatusSerializer(int_status.__dict__)
                return Response(serializer.data)
            else:
                return Response({'message':'NOT FOUND'})
        else:
            return Response({'message':'NOT SUFFICIENT OR ANY DATA SUPPLIED, PLEASE PASS THE ARGUMENTS project_id AND user_id'})

class SightNetworkViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    #permission_classes = [
    #    permissions.IsAuthenticated
    #]
    serializer_class = NeuronNetworkSerializer
    def list(self, request):
        if "user_id" in request.data and "project_id" in request.data:
            user_id=request.data['user_id']
            project_id=request.data['project_id']
            cur=connection.cursor()
            cur.execute('SELECT snb_s FROM brain WHERE user_id=%s AND id=%s',[user_id,project_id])
            pickled_data = cur.fetchone()
            sight_network=[]
            if pickled_data!=None:
                aux = pickle.loads(pickled_data[0])
                for i in aux.neuron_list:
                    if i._knowledge!=None:
                        sight_network.append(NeuronNetworkClass(i._has_knowledge,i._radius,i._degraded,json.dumps(i._knowledge.__dict__)))
                    else:
                        sight_network.append(NeuronNetworkClass(i._has_knowledge,i._radius,i._degraded,None))
                serializer = NeuronNetworkSerializer(instance=sight_network, many=True)
                return Response(serializer.data)
            else:
                return Response({'message':'NOT FOUND'})
        else:
            return Response({'message':'NOT SUFFICIENT OR ANY DATA SUPPLIED PLEASE, PASS THE ARGUMENTS project_id AND user_id'})


class HearingNetworkViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    #permission_classes = [
    #    permissions.IsAuthenticated
    #]
    serializer_class = NeuronNetworkSerializer
    def list(self, request):
        if "user_id" in request.data and "project_id" in request.data:
            user_id=request.data['user_id']
            project_id=request.data['project_id']
            cur=connection.cursor()
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



""" 
class testViewSet(viewsets.ViewSet):
    serializer_class = testSerializer
    def list(self, request):
        serializer = testSerializer()
        return Response(serializer.data)
 """

