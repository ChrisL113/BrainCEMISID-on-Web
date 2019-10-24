
class brain_state(object):
    def __init__(self,biology,cultural,feelings):
        self.biology =  biology
        self.cultural = cultural 
        self.feelings = feelings

class testClass(object):
    def __init__(self,test):
        self.test =  test

class SightNetworkClass(object):
    def __init__(self,_has_knowledge,_radius,_degraded,_knowledge):
        self._has_knowledge = _has_knowledge
        self._radius = _radius
        self._degraded = _degraded
        self._knowledge = _knowledge

#class HearingNetworkClass(object):
 #   def __init__(self,hearing_network):
  #      self.hearing_network = hearing_network

class HearingNetworkClass(object):
    def __init__(self,_has_knowledge,_radius,_degraded,_knowledge):
        self._has_knowledge = _has_knowledge
        self._radius = _radius
        self._degraded = _degraded
        self._knowledge = _knowledge


""" 
class Task(object):
    def __init__(self, **kwargs):
        for field in ('id', 'name', 'owner', 'status'):
            setattr(self, field, kwargs.get(field, None))

tasks = {
    1: Task(id=1, name='Demo', owner='xordoquy', status='Done'),
    2: Task(id=2, name='Model less demo', owner='xordoquy', status='Ongoing'),
    3: Task(id=3, name='Sleep more', owner='xordoquy', status='New'),
}


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=256)
    owner = serializers.CharField(max_length=256)

    def create(self, validated_data):
        return Task(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance 
        
class TaskViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = TaskSerializer

    def list(self, request):
        serializer = TaskSerializer(
            instance=tasks.values(), many=True)
        return Response(serializer.data)
        
        """