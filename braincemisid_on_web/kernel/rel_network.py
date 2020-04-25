import pickle

from neuron import Neuron

from brain.models import *
import json
## \defgroup RelBlocks Relational network related classes
#
# Relational network related classes are a group of classes that
# represent relational knowledge, neurons and networks
# @{
#



## Relational knowledge is a 3-tuple that
# relate a sight RbfNeuron id, a hearing RbfNeuron id and a  weight.
class RelKnowledge:

    ##  Create RelKnowledge instance given
    # a hearing id (id_h), sight id (id_s) and weight which defaults to zero
    def __init__(self, h_id, s_id, weight=0):
        self.set_h_id(h_id)
        self.set_s_id(s_id)
        self.set_weight(weight)

    ## Set hearing id
    # @param h_id Integer. Hearing id.
    def set_h_id(self, h_id):
        self._h_id = h_id

    ## Set sight id
    # @param s_id Integer. Sight id.
    def set_s_id(self, s_id):
        self._s_id = s_id

    ## Set weight
    # @param w Integer. Weight.
    def set_weight(self, w):
        if w >= 0:
            self._weight = w
        else:
            raise ValueError("Invalid value for w")

    ## Increase weight of relation by a given value
    # @param amount Integer Optional, 1 by default
    def increase_weight(self, amount=1):
        if self._weight + amount >= 0:
            self._weight += amount

    ## Get hearing id of relation
    # @retval h_id Integer. Hearing id.
    def get_h_id(self):
        return self._h_id

    ## Get sight id of relation
    # @retval s_id Integer. Sight id.
    def get_s_id(self):
        return self._s_id

    ## Get weight of relation
    # @retval weight Integer.
    def get_weight(self):
        return self._weight

    ## Return True if knowledge's hearing id is equal to given parameter h_id and
    # False in any other case
    def is_equal_hearing(self, h_id):
        return self._h_id == h_id

    ## Return True if knowledge sight id is equal to given parameter s_id and
    #   False in any other case
    def is_equal_sight(self, s_id):
        return self._s_id == s_id

    ## Return true if knowledge's sight id is equal to given parameter s_id and
    #  knowledge's hearing id is equal to given parameter h_id. Return false in any other case
    def is_equal(self, h_id, s_id):
        return self._h_id == h_id and self._s_id == s_id


## Relational neuron
class RelNeuron(Neuron):

    ## The constructor
    def __init__(self):
        super(RelNeuron, self).__init__()
        self._hit = False
        self.it_changed=False

    ## Set knowledge of type RelKnowledge
    # @param knowledge RelKnowledge to be learned
    def learn(self, knowledge):
        if isinstance(knowledge, RelKnowledge):
            self._knowledge = knowledge
            self._has_knowledge = True
        else:
            raise ValueError("value must be of type RelKnowledge")

    ## Set knowledge of type RelKnowledge
    # @param knowledge RelKnowledge to be learned
    def set_knowledge(self, knowledge):
        self.learn(knowledge)

    ## Return True if h_id is recognized as the hearing-id part of the RelKnowledge.
    # Also set an internal flag to indicate whether the last recognition process was successful (True)
    # or not (False). The value of the internal flag is accessible through the is_hit() method
    # @param h_id Integer. Hearing id.
    def recognize_hearing(self, h_id):
        if self.has_knowledge():
            self._hit = self._knowledge.is_equal_hearing(h_id)
        return self._hit

    ## Return true if s_id is recognized as the sight-id part of the relational knowledge.
    #     Also set an internal flag to indicate whether the last recognition process was successful (True)
    #    or not (False). The value of the internal flag is accessible through the is_hit() method
    # @param s_id Integer. Sight id.
    def recognize_sight(self, s_id):
        if self.has_knowledge():
            self._hit = self._knowledge.is_equal_sight(s_id)
        return self._hit

    ## Return hearing id if neuron has knowledge and an object of type None in any other case
    # @retval h_id Integer or None. Hearing id.
    def get_h_id(self):
        if self.has_knowledge():
            # Increase weight everytime that the relation is somehow used
            self._knowledge.increase_weight()
            self.it_changed=True
            return self._knowledge.get_h_id()
        return None

    ## Return sight id if neuron has knowledge and an object of type None in any other case
    # @retval s_id Integer or None. Sight id.
    def get_s_id(self):
        if self.has_knowledge():
            # Increase weight everytime that the relation is somehow used
            self._knowledge.increase_weight()
            self.it_changed=True
            return self._knowledge.get_s_id()
        return None

    ## Returns knowledge stored by neuron if neuron has knowledge,
    # and None object in any other case
    # @retval knowledge RelKnowledge or None.
    def get_knowledge(self):
        if self.has_knowledge():
            # Increase weight everytime that the relation is somehow used
            self._knowledge.increase_weight()
            self.it_changed=True
            return self._knowledge
        return None

    ##  Return weight of relation if neuron has knowledge and an object of type None in any other case
    # @retval weight Integer or None.
    def get_weight(self):
        if self.has_knowledge():
            return self._knowledge.get_weight()
        return None

    ## Set hearing id if neuron has knowledge. Raise an exception of type AttributeError if an attempt to
    # set the hearing id to a neuron with no previous knowledge is made
    # @param h_id Hearing id.
    def set_h_id(self, h_id):
        if self.has_knowledge():
            self._knowledge.set_h_id(h_id)
        else:
            raise AttributeError("neuron has no knowledge")

    ## Set sight id if neuron has knowledge. Raise an exception of type AttributeError if an attempt to
    # set the sight id to a neuron with no previous knowledge is made.
    # @param s_id Sight id
    def set_s_id(self, s_id):
        if self.has_knowledge():
            self._knowledge.set_s_id(s_id)
        else:
            raise AttributeError("neuron has no knowledge")

    ## Return true if neuron has h_id and s_id as hearing and sight ids respectively
    # @param h_id Hearing id
    # @param s_id Sight id
    def has_ids(self, h_id, s_id):
        return self._knowledge.is_equal(h_id, s_id)


## Relational network
class RelNetwork:

    ## The constructor
    # @param neuron_count Network size
    def __init__(self, neuron_count):
        # Create neuron list
        self.neuron_list = []
        # Fill neuron list with nre RelNeuron instances
        for index in range(neuron_count):
            self.neuron_list.append(RelNeuron())
        # Index of ready to learn neuron
        self._index_ready_to_learn = 0

    ##  Learn new knowledge in ready-to-learn neuron
    # @param knowledge RelKnowledge to be learned.
    def learn(self, knowledge):
        # If there is no capacity in neuron list, double size
        if self._index_ready_to_learn == (len(self.neuron_list)-1):
            new_list = []
            # Fill neuron list with nre RelNeuron instances
            for index in range(len(self.neuron_list)):
                new_list.append(RelNeuron())
            self.neuron_list = self.neuron_list + new_list
        # Check for neurons that already have given knowledge ids
        for index in range(self._index_ready_to_learn):
            if self.neuron_list[index].has_ids(knowledge.get_h_id(), knowledge.get_s_id()):
                return False
        # If there are no neurons with given pair of ids, learn
        self.neuron_list[self._index_ready_to_learn].learn(knowledge)
        self._index_ready_to_learn += 1
        return True

    ## Return a list of all knowledge in net such that it has parameter h_id as hearing id
    # @retval hearing_rels RelKnowledge vector
    def get_hearing_rels(self, h_id):
        # List of hearing relations
        hearing_rels = []
        for index in range(self._index_ready_to_learn):
            if self.neuron_list[index].recognize_hearing(h_id):
                hearing_rels.append(self.neuron_list[index].get_knowledge())
        return hearing_rels

    ## Return a list of all knowledge in net such that it has parameter s_id as sight id
    # @retval sight_rels RelKnowledge vector
    def get_sight_rels(self, s_id):
        # List of sight relations
        sight_rels = []
        for index in range(self._index_ready_to_learn):
            if self.neuron_list[index].recognize_sight(s_id):
                sight_rels.append(self.neuron_list[index].get_knowledge())
        return sight_rels

    ##  Returns number of neurons in network
    # @retval count Integer.
    def get_neuron_count(self):
        return len(self.neuron_list)

    @classmethod
    ## Serialize object and store it in given file
    # @param cls RelNetwork class
    # @param obj RelNetwork object to be serialized
    # @param name Name of the file where the serialization is to be stored
    def serialize(cls, obj, name, project_id, brain):
        if brain:
            if name=="rnb":
                rnb_data=rnb(brain_rnb=brain, index_ready_to_learn=obj._index_ready_to_learn)
                rnb_data.save()
                if obj.neuron_list:
                    for a in obj.neuron_list:
                        if a._knowledge!=None:
                            json_knowledge=json.dumps(a._knowledge.__dict__)
                            query_neuron=RnbNeuron(rnb=rnb_data, has_knowledge=a._has_knowledge, hit=a._hit, knowledge=json_knowledge)
                        else:
                            query_neuron=RnbNeuron(rnb=rnb_data, has_knowledge=a._has_knowledge, hit=a._hit)
                        query_neuron.save()


            elif name=="ss_rnb":
                ss_rnb_data=ss_rnb(brain_ss_rnb=brain, index_ready_to_learn=obj._index_ready_to_learn)
                ss_rnb_data.save()
                if obj.neuron_list:
                    for a in obj.neuron_list:
                        if a._knowledge!=None:
                            json_knowledge=json.dumps(a._knowledge.__dict__)
                            query_neuron=SsRnbNeuron(ss_rnb=ss_rnb_data, has_knowledge=a._has_knowledge, hit=a._hit, knowledge=json_knowledge)
                        else:
                            query_neuron=SsRnbNeuron(ss_rnb=ss_rnb_data, has_knowledge=a._has_knowledge, hit=a._hit)
                        query_neuron.save()

        else:
            if name=="rnb":

                rnb_data=rnb.objects.filter(brain_rnb__pk=project_id)
                rnb_data.update(index_ready_to_learn=obj._index_ready_to_learn)

                index_db=RnbNeuron.objects.filter(rnb__brain_rnb__pk=project_id).values('id').earliest('id')

                ind=0
                while ind < obj._index_ready_to_learn:
                    if obj.neuron_list[ind].it_changed:
                        neuron_from_db=RnbNeuron.objects.filter(pk=ind+index_db['id'])
                        neuron_from_db.update(has_knowledge=obj.neuron_list[ind]._has_knowledge, hit=obj.neuron_list[ind]._hit)
                    else:
                        if ind == obj._index_ready_to_learn-1:
                            json_knowledge=json.dumps(obj.neuron_list[ind]._knowledge.__dict__)
                            neuron_from_db=RnbNeuron.objects.filter(pk=ind+index_db['id'])
                            neuron_from_db.update(has_knowledge=obj.neuron_list[ind]._has_knowledge, hit=obj.neuron_list[ind]._hit, knowledge=json_knowledge)
                    ind +=1

            elif name=="ss_rnb":

                ss_rnb_data=ss_rnb.objects.filter(brain_ss_rnb__pk=project_id)
                ss_rnb_data.update(index_ready_to_learn=obj._index_ready_to_learn)

                index_db=SsRnbNeuron.objects.filter(ss_rnb_brain_ss_rnb__pk=project_id).values('id').earliest('id')
                ind=0
                while ind < obj._index_ready_to_learn:
                    if obj.neuron_list[ind].it_changed:
                        neuron_from_db=SsRnbNeuron.objects.filter(pk=ind+index_db['id'])
                        neuron_from_db.update(has_knowledge=obj.neuron_list[ind]._has_knowledge, hit=obj.neuron_list[ind]._hit)
                    else:
                        if ind == obj._index_ready_to_learn-1:
                            json_knowledge=json.dumps(obj.neuron_list[ind]._knowledge.__dict__)
                            neuron_from_db=SsRnbNeuron.objects.filter(pk=ind+index_db['id'])
                            neuron_from_db.update(has_knowledge=obj.neuron_list[ind]._has_knowledge, hit=obj.neuron_list[ind]._hit, knowledge=json_knowledge)
                    ind +=1

    @classmethod
    ## Deserialize object stored in given file
    # @param cls RelNetwork class
    # @param name Name of the file where the object is serialized
    def deserialize(cls, name, project_id):
        NEURON_COUNT=100
        if name=="rnb":
            rnb_data=rnb.objects.filter(brain_rnb__pk=project_id)
            neurons_from_db=RnbNeuron.objects.filter(rnb=rnb_data[0], has_knowledge=True).order_by('id')

            data=RelNetwork(NEURON_COUNT)
            data._index_ready_to_learn=rnb_data.values()[0]['index_ready_to_learn']

            ind=0
            for a in neurons_from_db.values():
                if a['has_knowledge']==True:
                    aux=json.loads(a['knowledge'])
                    data.neuron_list[ind]._has_knowledge=a['has_knowledge']
                    data.neuron_list[ind]._hit=a['hit']
                    aux_knowledge=RelKnowledge(aux['_h_id'], aux['_s_id'], aux['_weight']) 
                    data.neuron_list[ind].learn(aux_knowledge)
                ind +=1
            return data

        elif name=="ss_rnb":
            ss_rnb_data=ss_rnb.objects.filter(brain_ss_rnb__pk=project_id)
            neurons_from_db=SsRnbNeuron.objects.filter(ss_rnb=ss_rnb_data[0], has_knowledge=True).order_by('id')

            data=RelNetwork(NEURON_COUNT)
            data._index_ready_to_learn=ss_rnb_data.values()[0]['index_ready_to_learn']

            ind=0
            for a in neurons_from_db.values():
                if a['has_knowledge']==True:
                    aux=json.loads(a['knowledge'])
                    data.neuron_list[ind]._has_knowledge=a['has_knowledge']
                    data.neuron_list[ind]._hit=a['hit']
                    aux_knowledge=RelKnowledge(aux['_h_id'], aux['_s_id'], aux['_weight']) 
                    data.neuron_list[ind].learn(aux_knowledge)
                ind +=1
            return data



## @}
#

# Tests
if __name__ == '__main__':

    k1 = RelKnowledge(0, 0, 0)

    n1 = RelNeuron()

    print("N1 has knowledge: ", n1.has_knowledge())

    n1.learn(k1)

    print("N1 has knowledge: ", n1.has_knowledge())

    print("Neuron h_id ", n1.get_h_id())
    print("Neuron s_id ", n1.get_s_id())
    print("Neuron w ", n1.get_weight())

    n1.set_h_id(5)
    n1.set_s_id(-1)

    print("Neuron h_id ", n1.get_h_id())
    print("Neuron s_id ", n1.get_s_id())
    print("Neuron w ", n1.get_weight())

    # Create network of size 1
    net = RelNetwork(1)
    print("Size ", net.get_neuron_count())

    # Create vector of knowledge
    k = [RelKnowledge("1", 2, 5), RelKnowledge(1, 3, 5), RelKnowledge(2, 2), RelKnowledge(2, 3)]

    # Learn and see how network size increases
    for e in k:
        net.learn(e)
        print("Size ", net.get_neuron_count())

    # Get all hearing relations with id == 1
    for e in net.get_hearing_rels("1"):
        print("Sight:", e.get_s_id())
        print("Weight: ", e.get_weight())
