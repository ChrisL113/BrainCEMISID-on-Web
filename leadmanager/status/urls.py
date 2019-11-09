from rest_framework import routers
from .api import InternalStatusViewSet,DesiredStatusViewSet

router = routers.DefaultRouter()
router.register('api/internal_status', InternalStatusViewSet, 'internal_status')
router.register('api/desired_status', DesiredStatusViewSet, 'desired_status')
urlpatterns = router.urls