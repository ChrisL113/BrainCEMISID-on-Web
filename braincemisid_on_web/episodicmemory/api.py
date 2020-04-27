from rest_framework import  viewsets, permissions
from .serializers import  EpisodicMemorySerializer
from .classes import EpisodicMemoryClass
from rest_framework.response import Response
from django.db import connection

from django.contrib.auth.models import User
from brain.models import episodic_memory,group_episode
import pickle
import json

class EpisodicMemoryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = EpisodicMemorySerializer
    #pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        project_id=self.request.query_params.get('project_id')
        episodic_memory_data = episodic_memory.objects.filter(brain_episodic_memory__pk = project_id)
        group_from_db = group_episode.objects.filter(episodic_memory_group = episodic_memory_data[0]).order_by('id')
        knowl=None
        r1_aux=[]
        data=[]
        for k in group_from_db.values():
            
            r1_aux.append(k["episodicMemNeuron"])

        data.append(EpisodicMemoryClass(r1_aux,episodic_memory_data[0].clack,{'_recognized_indexes': episodic_memory_data[0].indexes_recognized}))
        r1_aux=[]
        serializer = EpisodicMemorySerializer(instance=data, many=True)
        return serializer.data