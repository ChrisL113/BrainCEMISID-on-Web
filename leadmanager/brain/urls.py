from rest_framework import routers
from .api import StatusViewSet,SightNetworkViewSet,HearingNetworkViewSet,testViewSet,ProjectViewset

router = routers.DefaultRouter()

router.register('api/overview', StatusViewSet, 'overview')
router.register('api/test', testViewSet, 'test')
router.register('api/sight_network', SightNetworkViewSet, 'sight_network' )
router.register('api/hearing_network', HearingNetworkViewSet, 'hearing_network')
router.register('api/projects', ProjectViewset, "projects")
urlpatterns = router.urls