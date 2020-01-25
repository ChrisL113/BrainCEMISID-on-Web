from rest_framework import viewsets, permissions
from .serializers import ImagesSettingsSerializer



class ImageSettingsSetViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ImagesSettingsSerializer

    def perform_create(self, serializer):
        #request.user.images_collection.filter()
        serializer.save(owner=self.request.user)