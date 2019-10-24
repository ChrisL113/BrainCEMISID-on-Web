from rest_framework import  viewsets, permissions
from .serializers import BrainStateSerializer, SightNetworkSerializer, HearingNetworkSerializer, testSerializer, ProjectSerializer
from .classes import brain_state, SightNetworkClass, HearingNetworkClass # classes
from rest_framework.response import Response

import sys

sys.path.append('D:\Desktop\BrainCEMISID on Web\leadmanager\kernel')

from kernel_braincemisid import KernelBrainCemisid
import json 

kernel = KernelBrainCemisid()
kernel_internal_state = kernel.get_internal_state().get_state()

status= brain_state(kernel_internal_state[0],kernel_internal_state[1],kernel_internal_state[2])


sight_network = []
hearing_network = []

for i in  kernel.snb.snb_s.neuron_list:
    if i._knowledge!=None:
        sight_network.append(SightNetworkClass(i._has_knowledge,i._radius,i._degraded,json.dumps(i._knowledge.__dict__)))
    else:
        sight_network.append(SightNetworkClass(i._has_knowledge,i._radius,i._degraded,None))

for i in  kernel.snb.snb_h.neuron_list:
    if i._knowledge!=None:
        hearing_network.append(HearingNetworkClass(i._has_knowledge,i._radius,i._degraded,json.dumps(i._knowledge.__dict__)))
    else:
        hearing_network.append(HearingNetworkClass(i._has_knowledge,i._radius,i._degraded,None))

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

# Brain Viewset
class StatusViewSet(viewsets.ViewSet):
    serializer_class = BrainStateSerializer
    def list(self, request):
        serializer = BrainStateSerializer(status)
        return Response(serializer.data)


class testViewSet(viewsets.ViewSet):
    serializer_class = testSerializer
    def list(self, request):
        serializer = testSerializer()
        return Response(serializer.data)

class SightNetworkViewSet(viewsets.ViewSet):
    serializer_class = testSerializer
    def list(self, request):
        serializer = SightNetworkSerializer(instance=sight_network, many=True)
        return Response(serializer.data)

class HearingNetworkViewSet(viewsets.ViewSet):
    serializer_class = HearingNetworkSerializer
    def list(self, request):
        serializer = HearingNetworkSerializer(instance=hearing_network, many=True)
        return Response(serializer.data)