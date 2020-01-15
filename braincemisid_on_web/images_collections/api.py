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
        return self.request.user.images_collection.all().order_by('id')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class AllCollectionsViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class= ImagesFromNeuronSerializer
    pagination_class = StandardResultsSetPagination
    queryset= ImagesFromNeuron.objects.all().order_by('id')
    permission_classes = [
        permissions.AllowAny
    ]

# class UserFilterImageViewSet(viewsets.ModelViewSet):
#     permission_classes = [
#         permissions.AllowAny#IsAuthenticated,
#     ]
#     serializer_class = ImagesFromNeuronSerializer

#     def get_queryset(self):
#         category_s= self.kwargs['category']
#         return ImagesFromNeuron.objects.filter(category=category_s)

