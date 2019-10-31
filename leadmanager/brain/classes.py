class KernelClass(object):
    def __init__(self,status,sight_network,hearing_network):
        self.status = status
        self.sight_network = sight_network
        self.hearing_network = hearing_network

class NeuronNetworkClass(object):
    def __init__(self,_has_knowledge,_radius,_degraded,_knowledge):
        self._has_knowledge = _has_knowledge
        self._radius = _radius
        self._degraded = _degraded
        self._knowledge = _knowledge

class StatusClass(object):
    def __init__(self,biology,culture,feelings):
        self.biology =  biology
        self.culture = culture 
        self.feelings = feelings

class BrainOutputClass(object):
    def __init__(self, h_knowledge,s_knowledge,state,internal_status):
        self.h_has_knowledge = h_knowledge._has_knowledge
        self.h_radius = h_knowledge._radius
        self.h_degraded = h_knowledge._degraded
        self.h_knowledge = h_knowledge._knowledge
        self.s_has_knowledge = s_knowledge._has_knowledge
        self.s_radius = s_knowledge._radius
        self.s_degraded = s_knowledge._degraded
        self.s_knowledge = s_knowledge._knowledge
        self.biology =  internal_status[0]
        self.culture = internal_status[1] 
        self.feelings = internal_status[2]
        self.state= state

""" 
class testClass(object):
    def __init__(self,test):
        self.test =  test """