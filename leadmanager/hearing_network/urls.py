from rest_framework import routers
from .api import HearingNetworkViewSet#,HearingNetProto

router = routers.DefaultRouter()
#router.register('api/hearing_proto', HearingNetProto, 'hearing_proto')
router.register('api/hearing_network', HearingNetworkViewSet, 'hearing_network')
urlpatterns = router.urls