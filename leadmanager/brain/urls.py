from rest_framework import routers
from .api import ProjectViewset,SightNetworkViewSet,HearingNetworkViewSet,InternalStatusViewSet,DesiredStatusViewSet,KernelViewSet

router = routers.DefaultRouter()
router.register('api/kernel', KernelViewSet, "kernel")
router.register('api/internal_status', InternalStatusViewSet, 'internal_status')
router.register('api/desired_status', DesiredStatusViewSet, 'desired_status')
#router.register('api/test', testViewSet, 'test')
router.register('api/sight_network', SightNetworkViewSet, 'sight_network' )
router.register('api/hearing_network', HearingNetworkViewSet, 'hearing_network')
router.register('api/projects', ProjectViewset, "projects")
urlpatterns = router.urls