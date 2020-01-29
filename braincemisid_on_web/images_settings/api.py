from rest_framework import viewsets, permissions, status
from .serializers import ImagesSettingsSerializer,ImageSettingsWithImageFromNeuron
from rest_framework.response import Response
from .models import ImageSettings
from brain.models import brain
import json

class ImageSettingsSetViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ImagesSettingsSerializer


    def create(self, request):
        #request.user.images_collection.filter()
        #print(request.data)
        if request.user.imageSettingsFromOwner.filter(image=request.data['image'],brain__id=request.data['brain']):
            #aux1=request.user.brain.objects#.imageSettingsFromBrain
            return Response({'message':'image_settings is already saved for this image in this project'})   
        if request.user.brain.filter(pk=request.data['brain']):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
            #  aux=ImageSettings(r_tolerance=request.data['r_tolerance'],g_tolerance=request.data['g_tolerance'],b_tolerance=request.data['b_tolerance'],owner=request.user)
            # aux.brain_id=request.data['brain']
            # aux.image_id=request.data['image']
            # aux.save()
            # return Response({'message':'done'})
        return Response(status=status.HTTP_400_BAD_REQUEST)
        #serializer.save(owner=self.request.user)
    def update(self, request,pk):
        id_image_s=pk
        image_to_update=request.user.imageSettingsFromOwner.get(pk=pk)
        serializer = self.serializer_class(image_to_update, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProjectImageSettings(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = ImageSettingsWithImageFromNeuron

    def get_queryset(self):
        project_id=self.request.query_params.get('project_id')
        return self.request.user.imageSettingsFromOwner.filter(brain=project_id).order_by('id')