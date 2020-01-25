from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import  UserSerializer,RegisterSerializer,LoginSerializer
from django.contrib.auth.models import User
#Register API

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        try:
            repeated=User.objects.filter(username=request.data['username']) | User.objects.filter(email=request.data['email'])
            if repeated:
                return Response ({"message" : "username or email already in use"})
            else:
                #print(request.data)
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.save()
                serialized_response=UserSerializer(user, context=self.get_serializer_context()).data
                auth=AuthToken.objects.create(user)[1]
                print(serialized_response,auth)
                return Response ({"user": serialized_response,"token": auth})
        except:
            return Response ({"message" : "not sufficient data :("})


#Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serialized_response=UserSerializer(user, context=self.get_serializer_context()).data
        auth=AuthToken.objects.create(user)[1]
        print(serialized_response)
        print("token :",auth)
        return Response ({
            "user": serialized_response,
            "token": auth
        })

# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user