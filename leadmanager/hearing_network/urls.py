from rest_framework import routers
from .api import HearingNeuronsViewSet

router = routers.DefaultRouter()
#router.register('api/hearing_proto', HearingNetProto, 'hearing_proto')
router.register('api/hearing_net', HearingNeuronsViewSet, 'hearing_net')
urlpatterns = router.urls