from rest_framework import  viewsets, permissions
from .serializers import ImagesFromNeuronSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from images_collections.models import ImagesFromNeuron
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class UserCollectionViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny#IsAuthenticated,
    ]
    serializer_class = ImagesFromNeuronSerializer
    pagination_class = StandardResultsSetPagination

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
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)