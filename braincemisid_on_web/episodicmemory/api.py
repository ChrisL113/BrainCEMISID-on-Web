from rest_framework import  viewsets, permissions
from .serializers import  EpisodicMemorySerializer
from .classes import EpisodicMemoryClass
from rest_framework.response import Response
from django.db import connection

from django.contrib.auth.models import User
import pickle
import json

# class EpisodicMemoryViewSet(viewsets.ViewSet):
#     #permission_classes = [
#     #    permissions.IsAuthenticated
#     #]
#     serializer_class = EpisodicMemorySerializer
#     def list(self, request):
#         if "user_id" in request.data and "project_id" in request.data:
#             user_id=request.data['user_id']
#             project_id=request.data['project_id']
#             with connection.cursor() as cur:
#                 cur.execute('SELECT episodic_memory FROM brain_brain WHERE user_id=%s AND id=%s',[user_id,project_id])
#                 pickled_data = cur.fetchone()
#             ind=1
#             episodic_memory=[]
#             if pickled_data!=None:
#                 aux = pickle.loads(pickled_data[0])
#                 #print(aux.group_list)
#                 for k in aux.group_list:
#                     for i in k.group:
#                         #print(i.__dict__)
#                         if i._knowledge!=None:
#                             if isinstance(i._knowledge, int):
#                                 #print(str(i._knowledge))
#                                 episodic_memory.append(EpisodicMemoryClass(i._has_knowledge,json.dumps(str(i._knowledge)),ind))
#                             else:
#                                 episodic_memory.append(EpisodicMemoryClass(i._has_knowledge,json.dumps(i._knowledge.__dict__),ind))
#                         else:
#                             episodic_memory.append(EpisodicMemoryClass(i._has_knowledge,None,ind))
#                         ind +=1
#                 serializer = EpisodicMemorySerializer(instance=episodic_memory, many=True)
#                 return Response(serializer.data)
#             else:
#                 return Response({'message':'NOT FOUND'})
#         else:
#             return Response({'message':'NOT SUFFICIENT OR ANY DATA SUPPLIED PLEASE, PASS THE ARGUMENTS project_id AND user_id'})

class EpisodicMemoryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = EpisodicMemorySerializer
    #pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        project_id=self.request.query_params.get('project_id')
        #print(self.request.user.brain.get(pk=project_id).episodic_memory)
        pickled_data=self.request.user.brain.get(pk=project_id).episodic_memory
        knowl=None
        r1_aux=[]
        r2_aux=[]
        episodic_memory=[]
        if pickled_data!=None:
            aux = pickle.loads(pickled_data)
            # print(aux.__dict__)
            for k in aux.group_list:
                for i in k.group:
                    
                    #if k.group!=[]:
                    #r1=json.dumps(k.group[0].__dict__)
                    if isinstance(i._knowledge, int):
                        knowl=i._knowledge
                    else:
                        knowl=i._knowledge.__dict__
                    
                    r2_aux.append({'has_knowledge':i._has_knowledge,'_knowledge':knowl})
                    #{'_has_knowledge':k.group[1]._has_knowledge,'_knowledge':k.group[1]._knowledge.__dict__}
                    #r2=json.dumps(r2_aux)
                    #k._index_bip
                if k.group!=[]:    
                    r2_aux.append({'index_bip':k._index_bip})
                    r1_aux.append(r2_aux)
                r2_aux=[]
            episodic_memory.append(EpisodicMemoryClass(r1_aux,aux._clack,{'_recognized_indexes':aux._recognized_indexes}))
            r1_aux=[]
                    #episodic_memory.append(EpisodicMemoryClass([json.dumps(k.group[0].__dict__),json.dumps(r2_aux),json.dumps(k._index_bip)]))
            serializer = EpisodicMemorySerializer(instance=episodic_memory, many=True)
            
            return serializer.data