from rest_framework import routers
from .api import HearingNetworkViewSet,SightNetProto

router = routers.DefaultRouter()
router.register('api/sight_proto', SightNetProto, 'sight_proto')
router.register('api/hearing_network', HearingNetworkViewSet, 'hearing_network')
urlpatterns = router.urls