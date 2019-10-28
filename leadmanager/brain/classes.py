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

class testClass(object):
    def __init__(self,test):
        self.test =  test