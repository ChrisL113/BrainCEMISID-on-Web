
class BrainOutputClass(object):
    def __init__(self, h_knowledge,s_knowledge,state,internal_status,desired_state):
        self.h_knowledge=h_knowledge
        self.s_knowledge = s_knowledge
        self.biology =  internal_status[0]
        self.culture = internal_status[1] 
        self.feelings = internal_status[2]
        self.desired_biology =  desired_state[0]
        self.desired_culture = desired_state[1] 
        self.desired_feelings = desired_state[2]
        self.state= state

""" 
class testClass(object):
    def __init__(self,test):
        self.test =  test """