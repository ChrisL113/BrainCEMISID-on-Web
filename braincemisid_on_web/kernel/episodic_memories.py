import pickle
from brain.models import *

from cultural_network import CulturalNetwork,CulturalGroup,CulturalNeuron
from internal_state import InternalState

import json

## \addtogroup Intentions
#  Episodic memories block
# @{

## The EpisodicMemoriesBlock is a specialization of CulturalNetwork
# from which a set of CulturalGroup s can be retrieved given a set of triggers, just
# as in humans. An exact memory can also be retrieved.
class EpisodicMemoriesBlock(CulturalNetwork):

    ## The constructor
    def __init__(self):
        CulturalNetwork.__init__(self)

    ## Return a list of memories (Cultural Groups) that contain the list of given
    # memory triggers
    # @retval retrieved_memories CulturalGroup vector.
    def retrieve_memories(self, trigger_list):
        # List of retrieved memories, initialized as and empty list
        retrieved_memories = []

        # For every trigger
        for trigger in trigger_list:
            # For every group (memory) in list of memories
            for group in self.group_list:
                # If the memory contains the given trigger
                if group.contains(trigger):
                    # Append the memory to list of retrieved memories
                    retrieved_memories.append(group)

        return retrieved_memories

    ##  Return the exact memory (except for last element in trigger)
    # @retval memory CulturalGroup
    def retrieve_exact_memory(self, trigger ):
        # Use bbcc protocol
        self.bum()
        for index in range(len(trigger)):
            if index != len(trigger)-1:
                self.bip(trigger[index])
            else:
                return self.group_list[self.check(trigger[index])]


    @classmethod
    ## Serialize object and store it in given file
    # @param cls EpisodicMemory class
    # @param obj EpisodicMemory object to be serialized
    # @param name Name of the file where the serialization is to be stored
    def serialize(cls, obj, name, project_id, brain):

        if brain:
            episodic_memory_data = episodic_memory(brain_episodic_memory = brain, index_ready_to_learn = obj._index_ready_to_learn, clack = obj._clack, indexes_recognized = obj._recognized_indexes)
            episodic_memory_data.save()

        else:
            episodic_memory_data = episodic_memory.objects.filter(brain_episodic_memory__pk = project_id)
            if episodic_memory_data[0].index_ready_to_learn < obj._index_ready_to_learn :
                knowl = None
                group_data = []
                index_alrdy_deprecated = None

                for i in obj.group_list[obj._index_ready_to_learn-1].group:

                    if isinstance(i._knowledge, int):
                        knowl = i._knowledge
                    else:
                        knowl = i._knowledge.__dict__

                    group_data.append({'has_knowledge': i._has_knowledge, '_knowledge': knowl})
                
                group_data.append({'index_bip': obj.group_list[obj._index_ready_to_learn-1]._index_bip})    
                query_group = group_episode(episodic_memory_group = episodic_memory_data[0], index_bip = obj.group_list[obj._index_ready_to_learn-1]._index_bip, episodicMemNeuron = group_data)
                query_group.save()

                episodic_memory_data.update(index_ready_to_learn = obj._index_ready_to_learn, clack = obj._clack, indexes_recognized = obj._recognized_indexes)

    @classmethod
    ## Deserialize object stored in given file
    # @param cls EpisodicMemory class
    # @param name Name of the file where the object is serialized
    def deserialize(cls, name, project_id):
        
        episodic_memory_data = episodic_memory.objects.filter(brain_episodic_memory__pk = project_id)
        group_from_db = group_episode.objects.filter(episodic_memory_group = episodic_memory_data[0]).order_by('id')

        
        data = EpisodicMemoriesBlock()

        it=None
        for i in group_from_db.values():

            it = len(i['episodicMemNeuron'])
            data.bum()

            for k in range(0, it-3):

                data.bip(i['episodicMemNeuron'][k]['_knowledge'])

            data.check(i['episodicMemNeuron'][-3]['_knowledge'])

            bcf = [i['episodicMemNeuron'][-2]['_knowledge']['biology'], i['episodicMemNeuron'][-2]['_knowledge']['culture'], i['episodicMemNeuron'][-2]['_knowledge']['feelings']]
            bcfState = InternalState(bcf)
            data.clack(bcfState)
            

        data._index_ready_to_learn = episodic_memory_data[0].index_ready_to_learn
        data._clack = episodic_memory_data[0].clack
        data._recognized_indexes = episodic_memory_data[0].indexes_recognized

        return data

## @}
#

# Tests
if __name__ == '__main__':

    em = EpisodicMemoriesBlock()

    # Learn a set of memories related to school
    # and its given [B C F]

    em.bum()
    em.bip('pencil')
    em.bip('eraser')
    em.check('sharpener')
    bcf = [0.1, 1, 0.6]
    em.clack(bcf)

    em.bum()
    em.bip('board')
    em.bip('eraser')
    em.check('pupils')
    bcf = [0.5, 0.7, 0.4]
    em.clack(bcf)

    em.bum()
    em.bip('board')
    em.bip('notebook')
    em.check('pupils')
    bcf = [0.4, 0.7, 0.4]
    em.clack(bcf)

    
    em.bum()
    em.bip('board')
    em.bip('notebook')
    em.check('pupils')
    bcf = [0.4, 0.7, 0.4]
    em.clack(bcf)

    # Test memories retrieval
    print("Retrieving memories related to 'house' ")
    if len(em.retrieve_memories(['house'])) == 0:
        print("No memories found")
    else:
        for memory in em.retrieve_memories(['house']):
            for episode in memory:
                print(episode.get_knowledge())

    print("Retrieving memories related to 'eraser'")
    if len(em.retrieve_memories(['eraser'])) == 0:
        print("No memories found")
    else:
        for memory in em.retrieve_memories(['eraser']):
            for episode in memory.group:
                print(episode.get_knowledge())

    print("Retrieving memories related to 'board and eraser'")
    if len(em.retrieve_memories(['board', 'eraser'])) == 0:
        print("No memories found")
    else:
        for memory in em.retrieve_memories(['board', 'eraser']):
            for episode in memory.group:
                print(episode.get_knowledge())