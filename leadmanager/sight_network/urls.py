from rest_framework import routers
from .api import SightNetworkViewSet,SightNeuronsViewSet

router = routers.DefaultRouter()
router.register('api/sight_network', SightNetworkViewSet, 'sight_network' )
router.register('api/sight_net', SightNeuronsViewSet, 'sight_net' )
urlpatterns = router.urls