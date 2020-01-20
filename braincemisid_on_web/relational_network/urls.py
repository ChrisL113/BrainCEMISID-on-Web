from rest_framework import routers
from .api import RelNetworkViewSet

router = routers.DefaultRouter()
router.register('api/rel_net', RelNetworkViewSet, "rel_net")

urlpatterns = router.urls