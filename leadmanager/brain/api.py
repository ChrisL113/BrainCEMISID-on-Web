from rest_framework import  viewsets, permissions,mixins
from .serializers import  NeuronNetworkSerializer,ProjectSerializer,StatusSerializer,BrainOutputSerializer
from .classes import NeuronNetworkClass,BrainOutputClass # classes
from rest_framework.response import Response

from django.db import connection
import pickle
import sys
import json

#################################### kernel################################################
sys.path.append('D:\Desktop\BrainCEMISID on Web\leadmanager\kernel')
from kernel_braincemisid import KernelBrainCemisid 
from sensory_neural_block import RbfKnowledge

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

class KernelViewSet(viewsets.ViewSet):
    kernel= None
    brain_output_serializer= None
    def pass_kernel_inputs(self, hearing_pattern, sight_pattern, hearing_class, intentions_input):
        # Set working domain
        if self.episodes_tgl_btn.state == "down":
            self.kernel.set_working_domain("EPISODES")
        else:
            self.kernel.set_working_domain("INTENTIONS")
            
        biology_in = intentions_input[0]
        culture_in = intentions_input[1]
        feelings_in= intentions_input[2]
        hearing_knowledge = RbfKnowledge(hearing_pattern, hearing_class)
        sight_knowledge = RbfKnowledge(sight_pattern, "NoClass")
        self.kernel.set_hearing_knowledge_in(hearing_knowledge)
        self.kernel.set_sight_knowledge_in(sight_knowledge)
        self.kernel.set_internal_state_in([biology_in, culture_in, feelings_in])
        self.kernel.set_desired_state([biology_in, culture_in, feelings_in])

    def show_kernel_outputs(self):
        internal_status = self.kernel.get_internal_state().get_state()
        if self.kernel.state == "HIT":
            h_knowledge = self.kernel.get_hearing_knowledge_out()
            s_knowledge = self.kernel.get_sight_knowledge_out()
            serializer_class = BrainOutputSerializer
            self.brain_output_serializer=BrainOutputClass(h_knowledge,s_knowledge,self.kernel.state,internal_status)

############################################### BBCC Protocole ###############################################

    def bum(self,hearing_pattern, sight_pattern, hearing_class, intentions_input):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input)
        self.kernel.bum()

    def bip(self,hearing_pattern, sight_pattern, hearing_class, intentions_input):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input)
        self.kernel.bip()
        self.show_kernel_outputs()

    def check(self,hearing_pattern, sight_pattern, hearing_class, intentions_input):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input)
        self.kernel.check()
        self.show_kernel_outputs()

    def clack(self,hearing_pattern, sight_pattern, hearing_class, intentions_input):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input)
        self.kernel.clack()
        self.show_kernel_outputs()

############################################## OTHER SIGNALS #############################################

    def set_zero(self,hearing_pattern, sight_pattern, hearing_class, intentions_input):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input)
        self.kernel.set_zero()

    def set_add_operator(self,hearing_pattern, sight_pattern, hearing_class, intentions_input):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input)
        self.kernel.set_add_operator()

    def set_equal_sign(self,hearing_pattern, sight_pattern, hearing_class, intentions_input):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input)
        self.kernel.set_equal_sign()

    def create(self,request):
        if "user_id" in request.data:
            frontend_request="POST"
            kernel=KernelBrainCemisid(request.data['user_id'],None,frontend_request)
            return Response({'message': kernel.message})

    def get(self,request):
        if "user_id" in request.data and "project_id" in request.data:
            frontend_request="GET"
            kernel=KernelBrainCemisid(request.data['user_id'],request.data['project_id'],frontend_request)
            return Response({'message': kernel.message })
        else:    
            return Response({'message':'NOT SUFFICIENT OR ANY DATA SUPPLIED, PLEASE PASS THE ARGUMENTS project_id AND user_id'})
    
    def put(self,request):
        ####################################### LEARNING #########################################
        if "action" in request.data and "hearing_pattern" in request.data and "sight_pattern" in request.data and "intentions_input" in request.data and "hearing_class" in request.data:
            print(request.data['hearing_pattern'])
            return Response({'message':'check bash'})
            if self.kernel==None:
                return Response({'message': 'KERNEL IS NOT LOADED'})
            
            if request.data['action'] == 'BUM':
                self.bum(request.data['hearing_pattern'],request.data['sight_pattern'],request.data['hearing_class'],request.data['intentions_input'])
                return Response({'message':'BBCC Protocole Initialized'})

            elif request.data['action'] == 'BIP':
                self.bip(request.data['hearing_pattern'],request.data['sight_pattern'],request.data['hearing_class'],request.data['intentions_input'])
                class_serializer
                return Response(brain_output_serializer.data)
            
            elif request.data['action'] == 'CHECK':
                self.check(request.data['hearing_pattern'],request.data['sight_pattern'],request.data['hearing_class'],request.data['intentions_input'])
                return Response(brain_output_serializer.data)
            
            elif request.data['action'] == 'CLACK':
                self.clack(request.data['hearing_pattern'],request.data['sight_pattern'],request.data['hearing_class'],request.data['intentions_input'])
                return Response(brain_output_serializer.data)
            
            elif request.data['action'] == 'SET_ZERO':
                self.set_zero(request.data['hearing_pattern'],request.data['sight_pattern'],request.data['hearing_class'],request.data['intentions_input'])
                return Response({'message':'SET_ZERO WAS SET IN BRAIN'})

            elif request.data['action'] == 'SET_ADD_OPERATOR':
                self.set_add_operator(request.data['hearing_pattern'],request.data['sight_pattern'],request.data['hearing_class'],request.data['intentions_input'])
                return Response({'message':'SET_ADD_OPERATOR WAS SET IN BRAIN'})

            elif request.data['action'] == 'SET_EQUAL_SIGN':
                self.set_equal_sign(request.data['hearing_pattern'],request.data['sight_pattern'],request.data['hearing_class'],request.data['intentions_input'])
                return Response({'message':'SET_EQUAL WAS SET IN BRAIN'})

        return Response({'message':'Missed'})
    
    def delete(self, request):
        if "user_id" in request.data and "project_id" in request.data:
            frontend_request="DELETE"
            kernel=KernelBrainCemisid(request.data['user_id'],request.data['project_id'],frontend_request)
            return Response({'message':kernel.message})
        else:    
            return Response({'message':'NOT SUFFICIENT OR ANY DATA SUPPLIED, PLEASE PASS THE ARGUMENTS project_id AND user_id'})
    

class InternalStatusViewSet(viewsets.ViewSet):
    #permission_classes = [
    #    permissions.IsAuthenticated
    #]
    serializer_class = StatusSerializer
    def list(self, request):
        if "user_id" in request.data and "project_id" in request.data:
            user_id=request.data['user_id']
            project_id=request.data['project_id']
            cur=connection.cursor()
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
            cur=connection.cursor()
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

class SightNetworkViewSet(viewsets.ViewSet):
    #permission_classes = [
    #    permissions.IsAuthenticated
    #]
    serializer_class = NeuronNetworkSerializer
    def list(self, request):
        if "user_id" in request.data and "project_id" in request.data:
            user_id=request.data['user_id']
            project_id=request.data['project_id']
            cur=connection.cursor()
            cur.execute('SELECT snb_s FROM brain WHERE user_id=%s AND id=%s',[user_id,project_id])
            pickled_data = cur.fetchone()
            sight_network=[]
            if pickled_data!=None:
                aux = pickle.loads(pickled_data[0])
                for i in aux.neuron_list:
                    if i._knowledge!=None:
                        sight_network.append(NeuronNetworkClass(i._has_knowledge,i._radius,i._degraded,json.dumps(i._knowledge.__dict__)))
                    else:
                        sight_network.append(NeuronNetworkClass(i._has_knowledge,i._radius,i._degraded,None))
                serializer = NeuronNetworkSerializer(instance=sight_network, many=True)
                return Response(serializer.data)
            else:
                return Response({'message':'NOT FOUND'})
        else:
            return Response({'message':'NOT SUFFICIENT OR ANY DATA SUPPLIED PLEASE, PASS THE ARGUMENTS project_id AND user_id'})


class HearingNetworkViewSet(viewsets.ViewSet):
    #permission_classes = [
    #    permissions.IsAuthenticated
    #]
    serializer_class = NeuronNetworkSerializer
    def list(self, request):
        if "user_id" in request.data and "project_id" in request.data:
            user_id=request.data['user_id']
            project_id=request.data['project_id']
            cur=connection.cursor()
            cur.execute('SELECT snb_h FROM brain WHERE user_id=%s AND id=%s',[user_id,project_id])
            pickled_data = cur.fetchone()
            hearing_network=[]
            if pickled_data!=None:
                aux = pickle.loads(pickled_data[0])
                for i in aux.neuron_list:
                    if i._knowledge!=None:
                        hearing_network.append(NeuronNetworkClass(i._has_knowledge,i._radius,i._degraded,json.dumps(i._knowledge.__dict__)))
                    else:
                        hearing_network.append(NeuronNetworkClass(i._has_knowledge,i._radius,i._degraded,None))
                serializer = NeuronNetworkSerializer(instance=hearing_network, many=True)
                return Response(serializer.data)
            else:
                return Response({'message':'NOT FOUND'})
        else:
            return Response({'message':'NOT SUFFICIENT OR ANY DATA SUPPLIED PLEASE, PASS THE ARGUMENTS project_id AND user_id'})



""" 
class testViewSet(viewsets.ViewSet):
    serializer_class = testSerializer
    def list(self, request):
        serializer = testSerializer()
        return Response(serializer.data)
 """

