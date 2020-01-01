from rest_framework import routers
from .api import KernelViewSet

router = routers.DefaultRouter()
router.register('api/kernel', KernelViewSet, "kernel")
#router.register('api/test', testViewSet, 'test')
urlpatterns = router.urls