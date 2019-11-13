from rest_framework import  viewsets, permissions
from .serializers import BrainOutputSerializer
from .classes import BrainOutputClass 
from rest_framework.response import Response

import pickle
import sys
import json

#################################### kernel################################################
sys.path.append('D:\Desktop\BrainCEMISID on Web\leadmanager\kernel')
from kernel_braincemisid import KernelBrainCemisid 
from sensory_neural_block import RbfKnowledge

class KernelViewSet(viewsets.ViewSet):
    kernel= None
    brain_output= None
    serializer_class = BrainOutputSerializer
    def pass_kernel_inputs(self, hearing_pattern, sight_pattern, hearing_class, intentions_input,is_episodes):
        # Set working domain
        if is_episodes == True:
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
            self.brain_output=BrainOutputClass(h_knowledge,s_knowledge,self.kernel.state,internal_status)

############################################### BBCC Protocole ###############################################

    def bum(self,hearing_pattern, sight_pattern, hearing_class, intentions_input,is_episodes):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input,is_episodes)
        self.kernel.bum()

    def bip(self,hearing_pattern, sight_pattern, hearing_class, intentions_input,is_episodes):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input,is_episodes)
        self.kernel.bip()
        self.show_kernel_outputs()

    def check(self,hearing_pattern, sight_pattern, hearing_class, intentions_input,is_episodes):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input,is_episodes)
        self.kernel.check()
        self.show_kernel_outputs()

    def clack(self,hearing_pattern, sight_pattern, hearing_class, intentions_input,is_episodes):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input,is_episodes)
        self.kernel.clack()
        self.show_kernel_outputs()

############################################## OTHER SIGNALS #############################################

    def set_zero(self,hearing_pattern, sight_pattern, hearing_class, intentions_input,is_episodes):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input,is_episodes)
        self.kernel.set_zero()

    def set_add_operator(self,hearing_pattern, sight_pattern, hearing_class, intentions_input,is_episodes):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input,is_episodes)
        self.kernel.set_add_operator()

    def set_equal_sign(self,hearing_pattern, sight_pattern, hearing_class, intentions_input,is_episodes):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input,is_episodes)
        self.kernel.set_equal_sign()

    def create(self,request):
        if "user_id" in request.data:
            frontend_request="POST"
            self.kernel=KernelBrainCemisid(request.data['user_id'],None,frontend_request)
            return Response({'message': self.kernel.message})
    
    def put(self,request):
        #################################################### LEARNING #########################################
        #if "action" in request.data and "hearing_pattern" in request.data and "sight_pattern" in request.data and "intentions_input" in request.data and "hearing_class" in request.data and "is_episodes" in request.data and "user_id" in request.data and "project_id" in request.data:
        frontend_request="GET"
        self.kernel=KernelBrainCemisid(request.data['user_id'],request.data['project_id'],frontend_request)
        #print(request.data)
        #return Response({'message':'check bash'})
        if self.kernel==None:
            return Response({'message': 'KERNEL IS NOT LOADED'})
            
        if "BUM" in request.data:
            for index in request.data['BUM']:
                self.bum(index['hearing_pattern'],index['sight_pattern'],index['hearing_class'],index['intentions_input'],request.data['is_episodes'])
                print("entering.. BUM")
                #return Response({'message':'BBCC Protocole Initialized'})

        if "BIP" in request.data:
            for index in request.data['BIP']:
                print("entering..BIP")
                self.bip(index['hearing_pattern'],index['sight_pattern'],index['hearing_class'],index['intentions_input'],request.data['is_episodes'])
                #return Response(serializer.data)
            
        if "CHECK" in request.data:
            for index in request.data['CHECK']:
                print("entering.... CHECK")
                self.check(index['hearing_pattern'],index['sight_pattern'],index['hearing_class'],index['intentions_input'],request.data['is_episodes'])
            
        if "CLACK" in request.data:
            for index in request.data['CLACK']:
                self.clack(index['hearing_pattern'],index['sight_pattern'],index['hearing_class'],index['intentions_input'],request.data['is_episodes'])
                return Response({'message':'DONE'})
        if not "CLACK" in request.data:
            serializer= BrainOutputSerializer(self.brain_output)
            return Response(serializer.data)
            
        #if "SET_ZERO" in request.data:
            #self.set_zero(request.data['hearing_pattern'],request.data['sight_pattern'],request.data['hearing_class'],request.data['intentions_input'],request.data['is_episodes'])
            #return Response({'message':'SET_ZERO WAS SET IN BRAIN'})

        #if "SET_ADD_OPERATOR" in request.data:
            #self.set_add_operator(request.data['hearing_pattern'],request.data['sight_pattern'],request.data['hearing_class'],request.data['intentions_input'],request.data['is_episodes'])
            #return Response({'message':'SET_ADD_OPERATOR WAS SET IN BRAIN'})

        #if "SET_EQUAL_SIGN" in request.data:
            #self.set_equal_sign(request.data['hearing_pattern'],request.data['sight_pattern'],request.data['hearing_class'],request.data['intentions_input'],request.data['is_episodes'])
            #return Response({'message':'SET_EQUAL WAS SET IN BRAIN'})
        
        return Response({'message':'Missed'})
    
    def delete(self, request):
        if "user_id" in request.data and "project_id" in request.data:
            frontend_request="DELETE"
            self.kernel=KernelBrainCemisid(request.data['user_id'],request.data['project_id'],frontend_request)
            return Response({'message':self.kernel.message})
        else:    
            return Response({'message':'NOT SUFFICIENT OR ANY DATA SUPPLIED, PLEASE PASS THE ARGUMENTS project_id AND user_id'})
    

""" 
class testViewSet(viewsets.ViewSet):
    serializer_class = testSerializer
    def list(self, request):
        serializer = testSerializer()
        return Response(serializer.data)
 """

