from rest_framework import  viewsets, permissions
from .serializers import ImagesFromNeuronSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from images_collections.models import ImagesFromNeuron



class UserCollectionViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny#IsAuthenticated,
    ]
    serializer_class = ImagesFromNeuronSerializer

    def get_queryset(self):
        return self.request.user.images_collection.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class AllCollectionsViewSet(viewsets.ModelViewSet):
    
    queryset= ImagesFromNeuron.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class= ImagesFromNeuronSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)