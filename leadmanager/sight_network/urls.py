from rest_framework import routers
from .api import SightNetworkViewSet

router = routers.DefaultRouter()
router.register('api/sight_network', SightNetworkViewSet, 'sight_network' )
urlpatterns = router.urls