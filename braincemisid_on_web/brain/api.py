from rest_framework import  viewsets, permissions
from .serializers import BrainOutputSerializer,ProjectSummarySerializer
from .classes import BrainOutputClass 
from rest_framework.response import Response

import pickle
import sys
import json
import os 
dirname = os.path.dirname(__file__) 
filename = os.path.join(os.path.realpath('.'), 'kernel')

sys.path.append(filename)

from kernel_braincemisid import KernelBrainCemisid 
from sensory_neural_block import RbfKnowledge

from .models import *
from images_collections.models import *

class KernelViewSet(viewsets.ViewSet):
    kernel= None
    h_knowledge=[]
    s_knowledge=[]
    brain_output= []
    serializer_class = BrainOutputSerializer
    def pass_kernel_inputs(self, hearing_pattern, sight_pattern, hearing_class, intentions_input, desired_input, mode):
        # Set working domain
        if mode== "EPISODES":
            self.kernel.set_working_domain("EPISODES")
        elif mode=="INTENTIONS":
            self.kernel.set_working_domain("INTENTIONS")
        elif mode=="ADDITION":
            self.kernel.set_working_domain("ADDITION")
        elif mode== "COUNTING":
            self.kernel.set_working_domain("COUNTING")
        elif mode== "READING":
            self.kernel.set_working_domain("READING")

        biology_in = intentions_input[0]
        culture_in = intentions_input[1]
        feelings_in= intentions_input[2]
        hearing_knowledge = RbfKnowledge(hearing_pattern, hearing_class)
        sight_knowledge = RbfKnowledge(sight_pattern, "NoClass")

        self.kernel.set_hearing_knowledge_in(hearing_knowledge)
        self.kernel.set_sight_knowledge_in(sight_knowledge)
        self.kernel.set_internal_state_in([biology_in, culture_in, feelings_in])
        
        desired_biology_in = desired_input[0]
        desired_culture_in = desired_input[1]
        desired_feelings_in= desired_input[2]
        # desired_biology_in = intentions_input[0]
        # desired_culture_in = intentions_input[1] 
        # desired_feelings_in= intentions_input[2]
        self.kernel.set_desired_state([desired_biology_in, desired_culture_in, desired_feelings_in])

    def show_kernel_outputs(self):
        internal_status = self.kernel.get_internal_state().get_state()
        desired_status = self.kernel.get_desired_state().get_state()
        if self.kernel.state == "HIT":
            self.h_knowledge = self.kernel.get_hearing_knowledge_out()
            self.s_knowledge = self.kernel.get_sight_knowledge_out()
            #self.brain_output=BrainOutputClass(h_knowledge,s_knowledge,self.kernel.state,internal_status)
            self.brain_output=[]
            if isinstance(self.s_knowledge, list):
                index=0
                
                print("im entering and doing what you needed...")
                for h,s in self.h_knowledge,self.s_knowledge:
                    if index==0:
                        self.brain_output.append(BrainOutputClass(h,s,self.kernel.state,internal_status))
                    else:
                        self.brain_output.append(BrainOutputClass(h,s,None,None))
                    index +=1
            else:
                self.brain_output.append(BrainOutputClass(self.h_knowledge,self.s_knowledge,self.kernel.state,internal_status,desired_status))
############################################### BBCC Protocole ###############################################

    def bum(self,hearing_pattern, sight_pattern, hearing_class, intentions_input, desired_input, mode):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input, desired_input, mode)
        self.kernel.bum()

    def bip(self,hearing_pattern, sight_pattern, hearing_class, intentions_input, desired_input, mode):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input, desired_input, mode)
        self.kernel.bip()
        self.show_kernel_outputs()

    def check(self,hearing_pattern, sight_pattern, hearing_class, intentions_input, desired_input, mode):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input, desired_input, mode)
        self.kernel.check()
        self.show_kernel_outputs()

    def clack(self,hearing_pattern, sight_pattern, hearing_class, intentions_input, desired_input, mode):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input, desired_input, mode)
        self.kernel.clack()
        self.show_kernel_outputs()

############################################## OTHER SIGNALS #############################################

    def set_zero(self,hearing_pattern, sight_pattern, hearing_class, intentions_input, desired_input, mode):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input, desired_input, mode)
        self.kernel.set_zero()

    def set_add_operator(self,hearing_pattern, sight_pattern, hearing_class, intentions_input, desired_input, mode):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input, desired_input, mode)
        self.kernel.set_add_operator()

    def set_equal_sign(self,hearing_pattern, sight_pattern, hearing_class, intentions_input, desired_input, mode):
        self.pass_kernel_inputs(hearing_pattern, sight_pattern, hearing_class, intentions_input, desired_input, mode)
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
        
        if "SET_ZERO" in request.data:
            self.set_zero(request.data['SET_ZERO']['hearing_pattern'],request.data['SET_ZERO']['sight_pattern'],request.data['SET_ZERO']['hearing_class'],request.data['SET_ZERO']['intentions_input'],request.data['SET_ZERO']['desired_intentions_input'],request.data['mode'])
            
            if self.kernel.hearing_id!=-1:
                return Response({'message':'FROM SET_ZERO, its already set the neuron is', 'id':self.kernel.hearing_id})
            else:
                return Response({'message':'FROM SET_ZERO, THERE IS NO SUCH A NEURON'})

        if "SET_ADD_OPERATOR" in request.data:
            self.set_add_operator(request.data['SET_ADD_OPERATOR']['hearing_pattern'],request.data['SET_ADD_OPERATOR']['sight_pattern'],request.data['SET_ADD_OPERATOR']['hearing_class'],request.data['SET_ADD_OPERATOR']['intentions_input'],request.data['SET_ADD_OPERATOR']['desired_intentions_input'],request.data['mode'])
            
            if self.kernel.hearing_id!=-1:
                return Response({'message':'FROM SET_ADD_OPERATOR, its already set the neuron is', 'id':self.kernel.hearing_id})
            else:
                return Response({'message':'FROM SET_ADD_OPERATOR, THERE IS NO SUCH A NEURON'})

        if "SET_EQUAL_SIGN" in request.data:
            state_operator=self.set_equal_sign(request.data['SET_EQUAL_SIGN']['hearing_pattern'],request.data['SET_EQUAL_SIGN']['sight_pattern'],request.data['SET_EQUAL_SIGN']['hearing_class'],request.data['SET_EQUAL_SIGN']['intentions_input'],request.data['SET_EQUAL_SIGN']['desired_intentions_input'],request.data['mode'])
            if self.kernel.hearing_id!=-1:
                return Response({'message':'FROM SET_EQUAL_SIGN, SET_EQUAL WAS SET IN BRAIN, THE NEURON ID IS', 'id':self.kernel.hearing_id})
            else:
                return Response({'message':'FROM SET_EQUAL_SIGN, THERE IS NO SUCH A NEURON'})
                
        if "BUM" in request.data:
            for index in request.data['BUM']:
                self.bum(index['hearing_pattern'],index['sight_pattern'],index['hearing_class'],index['intentions_input'],index['desired_intentions_input'], request.data['mode'])
                print("entering.. BUM")
                #return Response({'message':'BBCC Protocole Initialized'})

        if "BIP" in request.data:
            for index in request.data['BIP']:
                print("entering..BIP")
                self.bip(index['hearing_pattern'],index['sight_pattern'],index['hearing_class'],index['intentions_input'],index['desired_intentions_input'], request.data['mode'])
                #return Response(serializer.data)
            
        if "CHECK" in request.data:
            for index in request.data['CHECK']:
                print("entering.... CHECK")
                self.check(index['hearing_pattern'],index['sight_pattern'],index['hearing_class'],index['intentions_input'],index['desired_intentions_input'], request.data['mode'])
            
        if "CLACK" in request.data:
            # qifn=ImagesFromNeuron(owner=user,name="lo que sea", name_class="asdfjksl")
            # print(qifn)
            # qifn.save()

            #qifn.save()
            for index in request.data['CLACK']:
                self.clack(index['hearing_pattern'],index['sight_pattern'],index['hearing_class'],index['intentions_input'],index['desired_intentions_input'], request.data['mode'])
                if  index['image_id']==-1:
                        return Response({'message':'neuron saved but wihout image because of debugging options'})
                if ImagesFromNeuron.objects.filter(pk=index['image_id']):
                    
                    neuron_from_db=RbfNeuronSight.objects.filter(pk=self.kernel.snb.snb_s._last_learned_id_from_db).values('img_id')
                    if  neuron_from_db[0]['img_id']==None and "image_id" in index or "image_id" in index and index['rename']==True:   
                        #print(index['image_id'])
                        #print(neuron_from_db[0])
                        neuron_from_db.update(img_id=index['image_id'])
                        print("entering...")
                        if index['rename']==True:
                            return Response({'message':'renamed with image id:','id':index['image_id']})
                        else:
                            return Response({'message':'paired with image id','id':index['image_id']})
                    if neuron_from_db[0]['img_id']==index['image_id']:
                        return Response({'message':'this id is already in the neuron','id':index['image_id']})
                    if neuron_from_db[0]['img_id']!=index['image_id']:
                        return Response({'message':'there is another id in the neuron, if you want to rename it please, pass the argument rename equal to true, otherwise the id is','id':neuron_from_db[0]['img_id']})
                else:
                    return Response({'message':'there is not id like this'})

        if not "CLACK" in request.data:
            #serializer= BrainOutputSerializer(self.brain_output)
            serializer= BrainOutputSerializer(instance=self.brain_output, many=True)
            return Response(serializer.data)
        
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



class ProjectSummaryViewSet(viewsets.ModelViewSet):
    permission_classes = [
            permissions.AllowAny#IsAuthenticated,
        ]
    serializer_class = ProjectSummarySerializer
    #pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return self.request.user.brain.all()
