from rest_framework import  viewsets, permissions
from .serializers import NeuronHearingSerializer

from rest_framework.response import Response
#from django.contrib.auth.models import User
from brain.models import RbfNeuronHearing

class HearingNeuronsViewSet(viewsets.ViewSet):
    #permission_classes = [
    #    permissions.IsAuthenticated
    #]

    def list(self, request):
        
        if  "project_id" in request.data:
            
            project_id=request.data['project_id']
            try:
                query=RbfNeuronHearing.objects.filter(snb_hearing__brain_h__pk=project_id, has_knowledge=True)
                #print(query.values())
                serializer = NeuronHearingSerializer(instance=query, many=True)
            except:
                return Response({'message':'There was an error, please, check the project_id'})
        
            return Response(serializer.data)