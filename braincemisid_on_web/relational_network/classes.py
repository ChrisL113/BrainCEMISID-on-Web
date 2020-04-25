
class RelNetworkClass(object):
    def __init__(self, _hit,_knowledge,has_knowledge):
        self._has_knowledge=has_knowledge
        self._hit=_hit
        self._h_id= _knowledge['_h_id']
        self._s_id=_knowledge['_s_id']
        self._weight=_knowledge['_weight']