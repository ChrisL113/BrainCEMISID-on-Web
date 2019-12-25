import pickle

import psycopg2
import logging
from psycopg2 import extras
from datetime import datetime
from psycopg2 import sql

from cultural_network import CulturalNetwork,CulturalGroup,CulturalNeuron

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
        
        query = sql.SQL("UPDATE brain_brain SET {} = %s WHERE id=%s").format(sql.Identifier(name))

        cur.execute(query, (pickled_obj,project_id,))

        conn.commit()
        cur.close()
        conn.close()


    @classmethod
    ## Deserialize object stored in given file
    # @param cls EpisodicMemory class
    # @param name Name of the file where the object is serialized
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

        query = sql.SQL("SELECT {} FROM brain_brain WHERE id=%s").format(sql.Identifier(name))
        cur.execute(query, (project_id,))
        
        pickled_data = cur.fetchone()

        return pickle.loads(pickled_data[0])
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