from rest_framework import viewsets, permissions
from .serializers import ImagesSettingsSerializer,ImageSettingsWithImageFromNeuron
from rest_framework.response import Response
from .models import ImageSettings
import json

class ImageSettingsSetViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ImagesSettingsSerializer

    def create(self, request):
        #request.user.images_collection.filter()
        #print(request.data)
        if request.user.imageSettings.filter(image=request.data['image'],brain__id=request.data['brain']):
            return Response({'message':'you are now in db'})     
        if request.user.brain.filter(pk=request.data['brain']):
            aux=ImageSettings(r_tolerance=request.data['r_tolerance'],g_tolerance=request.data['g_tolerance'],b_tolerance=request.data['b_tolerance'],owner=request.user)
            aux.brain_id=request.data['brain']
            aux.image_id=request.data['image']
            aux.save()
            return Response({'message':'done'})
        return Response({'message':'error this user has not this project id'})
        #serializer.save(owner=self.request.user)

class ProjectImageSettings(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = ImageSettingsWithImageFromNeuron

    def get_queryset(self):
        project_id=self.request.query_params.get('project_id')
        return self.request.user.imageSettings.filter(brain=project_id).order_by('id')