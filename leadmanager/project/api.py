from rest_framework import  viewsets, permissions
from .serializers import ProjectSerializer
from rest_framework.response import Response

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
