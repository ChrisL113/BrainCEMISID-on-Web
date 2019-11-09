
class BrainOutputClass(object):
    def __init__(self, h_knowledge,s_knowledge,state,internal_status):
        self.h_pattern = h_knowledge._pattern
        self.hearing_class=h_knowledge._class
        self.s_pattern = s_knowledge._pattern
        self.neuron_number = s_knowledge._class
        self.biology =  internal_status[0]
        self.culture = internal_status[1] 
        self.feelings = internal_status[2]
        self.state= state

""" 
class testClass(object):
    def __init__(self,test):
        self.test =  test """