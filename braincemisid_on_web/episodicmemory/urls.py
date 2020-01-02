from rest_framework import routers
from .api import EpisodicMemoryViewSet

router = routers.DefaultRouter()
#router.register('api/sight_network', SightNetworkViewSet, 'sight_network' )
router.register('api/episodicmemory',  EpisodicMemoryViewSet, 'episodicmemory' )
urlpatterns = router.urls