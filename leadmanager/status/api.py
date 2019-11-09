from rest_framework import  viewsets, permissions
from .serializers import StatusSerializer
from rest_framework.response import Response

from django.db import connection
import pickle

class InternalStatusViewSet(viewsets.ViewSet):
    #permission_classes = [
    #    permissions.IsAuthenticated
    #]
    serializer_class = StatusSerializer
    def list(self, request):
        if "user_id" in request.data and "project_id" in request.data:
            user_id=request.data['user_id']
            project_id=request.data['project_id']
            with connection.cursor() as cur:
                cur.execute('SELECT internal_state FROM brain WHERE user_id=%s AND id=%s',[user_id,project_id])
                pickled_data = cur.fetchone()
            if pickled_data!=None:
                int_status=pickle.loads(pickled_data[0])
                serializer = StatusSerializer(int_status.__dict__)
                return Response(serializer.data)
            else:
                return Response({'message':'NOT FOUND'})
        else:
            return Response({'message':'NOT SUFFICIENT OR ANY DATA SUPPLIED, PLEASE PASS THE ARGUMENTS project_id AND user_id'})

class DesiredStatusViewSet(viewsets.ViewSet):
    #permission_classes = [
    #    permissions.IsAuthenticated
    #]
    serializer_class = StatusSerializer
    def list(self, request):
        if "user_id" in request.data and "project_id" in request.data:
            user_id=request.data['user_id']
            project_id=request.data['project_id']
            with connection.cursor() as cur:
                cur.execute('SELECT desired_state FROM brain WHERE user_id=%s AND id=%s',[user_id,project_id])
                pickled_data = cur.fetchone()
            if pickled_data!=None:
                int_status=pickle.loads(pickled_data[0])
                serializer = StatusSerializer(int_status.__dict__)
                return Response(serializer.data)
            else:
                return Response({'message':'NOT FOUND'})
        else:
            return Response({'message':'NOT SUFFICIENT OR ANY DATA SUPPLIED, PLEASE PASS THE ARGUMENTS project_id AND user_id'})
