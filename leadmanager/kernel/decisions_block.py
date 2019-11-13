import pickle

import psycopg2
import logging
from psycopg2 import extras
from datetime import datetime
from psycopg2 import sql

from unconscious_filtering_block import UnconsciousFilteringBlock
from conscious_decisions_block import ConsciousDecisionsBlock

## \addtogroup Intentions
#  Decisions block
# @{

## The DecisionsBlock takes as input a set of memories (CulturalGroup)
# and gives as output one of them from which the decision can be inferred.
#
# For example, is the input are two memories, one related to ice cream and the other to soccer,
# the output could be the one related to soccer, so the decision is to play soccer.
class DecisionsBlock:

    ## The constructor
    def __init__(self):
        # Ports
        self.input_memories = None
        self.conscious_output = None
        self.unconscious_output = None
        self.internal_state = None
        self.desired_state = None

        self.unconscious_block = UnconsciousFilteringBlock()
        self.conscious_block = ConsciousDecisionsBlock()

    ## Set input memories
    # @param input_memories CulturalGroup vector where the last element is of type BiologyCultureFeelings (memories)
    def set_input_memories(self, input_memories):
        self.input_memories = input_memories

    ## Set entity's internal state
    # @param internal_state InternalState
    def set_internal_state(self, internal_state ):
        self.internal_state = internal_state

    ## Set entity's desired state
    # @param desired_state InternalState
    def set_desired_state(self, desired_state ):
        self.desired_state = desired_state

    ## Get output memory
    # @retval output CulturalGroup. The memory from which the decision can be inferred.
    def get_output_memory(self):
        self.unconscious_block.set_internal_state(self.internal_state)
        self.unconscious_block.set_desired_state(self.desired_state)
        self.unconscious_block.set_inputs(self.input_memories)
        self.unconscious_output = self.unconscious_block.get_outputs()
        self.conscious_block.set_desired_state(self.desired_state)
        self.conscious_block.set_internal_state(self.internal_state)
        conscious_inputs = []
        for memory in self.unconscious_output:
            conscious_inputs.append(memory.get_tail_knowledge())
        self.conscious_block.set_inputs(conscious_inputs)
        conscious_output_index = self.conscious_block.get_decision()
        self.conscious_output = self.unconscious_output[conscious_output_index]
        return self.conscious_output

    @classmethod
    ## Serialize object and store in given file
    # @param cls CulturalNetwork class
    # @param obj CulturalNetwork object to be serialized
    # @param name Name of the file where the serialization is to be stored
    def serialize(cls, obj, name, project_id):
        #pickle.dump(obj, open(name, "wb"))
        try:
            conn = psycopg2.connect(dbname='braincemisid_db', user='postgres', host='localhost',password='1234')
            print("Opened db successfully.", name)
        except:
            print("Unable to connect to the database")
            logging.exception('Unable to open database connection')
            return
        else:
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        pickled_obj = pickle.dumps(obj)
        
        query = sql.SQL("UPDATE brain_projects SET {} = %s WHERE id=%s").format(sql.Identifier(name))

        cur.execute(query, (pickled_obj,project_id,))

        conn.commit()
        cur.close()
        conn.close()


    @classmethod
    ## Deserialize object stored in given file
    # @param cls CulturalNetwork class
    # @param name Name of the file where the object is serialize
    def deserialize(cls, name, project_id):
        try:
            conn = psycopg2.connect(dbname='braincemisid_db', user='postgres', host='localhost',
                                password='1234')
            print("Opened db successfully", name)
        except:
            print(datetime.now(), "Unable to connect to the database")
            logging.exception('Unable to open database connection')
        else:
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        query = sql.SQL("SELECT {} FROM brain_projects WHERE id=%s").format(sql.Identifier(name))
        cur.execute(query, (project_id,))
        
        pickled_data = cur.fetchone()

        return pickle.loads(pickled_data[0])
## @}
#


# Tests
if __name__ == '__main__':

    from cultural_network import CulturalGroup
    from internal_state import InternalState,BiologyCultureFeelings

    # Memories
    MEMORIES_COUNT = 6
    memories = [CulturalGroup() for i in range(MEMORIES_COUNT)]
    import random

    bcf = []
    for i in range(MEMORIES_COUNT):
        memories[i].bum()
        memories[i].learn(i)
        bcf.append(BiologyCultureFeelings())
        new_state = [random.random(), random.random(), random.random()]
        bcf[i].set_state(new_state)
        memories[i].clack(bcf[i])
        print("Memory ", i, " bcf is", memories[i].get_tail_knowledge().get_state())

    d_block = DecisionsBlock()
    internal_state = InternalState()
    internal_state.set_state([0.5, 1, 1])
    d_block.set_internal_state(internal_state)
    desired_state = InternalState()
    desired_state.set_state([0.5, 1, 1])
    d_block.set_desired_state(desired_state)
    d_block.set_input_memories(memories)
    output = d_block.get_output_memory()
    print("Decisions Block output is ", output.get_tail_knowledge().get_state())
    print("made by ", d_block.conscious_block.get_last_decision_type())
    print("Unconscious decisions ")
    for mem in d_block.unconscious_output:
        print(mem.get_tail_knowledge().get_state())