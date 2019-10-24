from rest_framework import routers
from .api import LeadViewSet,StatusViewSet, SightNetworkViewSet,HearingNetworkViewSet,testViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
router.register('api/overview', StatusViewSet, 'overview')
router.register('api/test', testViewSet, 'test')
router.register('api/sight_network', SightNetworkViewSet, 'sight_network' )
router.register('api/hearing_network', HearingNetworkViewSet, 'hearing_network')
urlpatterns = router.urls