from rest_framework import  viewsets, permissions
from .serializers import BrainOutputSerializer
from .classes import BrainOutputClass 
from rest_framework.response import Response

import pickle
import sys
import json

#################################### kernel################################################
sys.path.append('D:\Desktop\BrainCEMISID on Web\\braincemisid_on_web\kernel')
from kernel_braincemisid import KernelBrainCemisid 
from sensory_neural_block import RbfKnowledge

from .models import *
from images_collections.models import *

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
        if "user_id" and "project_name" in request.data:
            frontend_request="POST"
            user = User.objects.get(pk=request.data['user_id'])
            if user!=None:
                self.kernel=KernelBrainCemisid(user,request.data,frontend_request)
                return Response({'message': self.kernel.message})
            else:
                return Response({'message': 'THERE IS NO USER WITH THIS ID'})
        else:
            return Response({'message': 'INVALID / NOT SUFFICIENT DATA'})

    def put(self,request):
        #################################################### LEARNING #########################################
        if "user_id" in request.data:
            frontend_request="PUT"
            user = User.objects.get(pk=request.data['user_id'])
            self.kernel=KernelBrainCemisid(user,request.data,frontend_request)
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
            # qifn=ImagesFromNeuron(owner=user,name="lo que sea", name_class="asdfjksl")
            # print(qifn)
            # qifn.save()

            #qifn.save()
            for index in request.data['CLACK']:
                self.clack(index['hearing_pattern'],index['sight_pattern'],index['hearing_class'],index['intentions_input'],request.data['is_episodes'])
                if ImagesFromNeuron.objects.filter(pk=request.data['image_id']):
                    neuron_from_db=RbfNeuronSight.objects.filter(pk=self.kernel.snb.snb_s._last_learned_id_from_db).values('img_id')
                    if  neuron_from_db[0]['img_id']==None and "image_id" in request.data or "image_id" in request.data and request.data['rename']==True:   
                        #print(request.data['image_id'])
                        #print(neuron_from_db[0])
                        neuron_from_db.update(img_id=request.data['image_id'])
                        
                        if request.data['rename']==True:
                            return Response({'message':'renamed with image id:','id':request.data['image_id']})
                        else:
                            return Response({'message':'paired with image id','id':request.data['image_id']})
                        
                    if neuron_from_db[0]['img_id']==request.data['image_id']:
                        return Response({'message':'this id is already in the neuron','id':request.data['image_id']})
                    if neuron_from_db[0]['img_id']!=request.data['image_id']:
                        return Response({'message':'there is another id in the neuron, if you want to rename it please, pass the argument rename equal to true, otherwise the id is','id':neuron_from_db[0]['img_id']})
                else:
                    return Response({'message':'there is not id like this'})

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
        
        return Response({'message':'MISSED'})
    
    def delete(self, request):
        if "project_id" in request.data :
            try:
                query = brain.objects.get(pk=request.data['project_id'])
            except:
                return Response({'message':'NOT BRAIN WAS FOUND TO DELETE'})
            
            query.delete()
            return Response({'message':'BRAIN SUCCESFULLY DELETED'})

        else:    
            return Response({'message':'NOT PARAMETER project_id WAS PROVIDED'})
    
# class testViewSet(viewsets.ViewSet):
#     serializer_class = testSerializer
#     def list(self, request):
#         serializer = testSerializer()
#         return Response(serializer.data)


