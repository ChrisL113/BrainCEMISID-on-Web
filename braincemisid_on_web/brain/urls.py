from rest_framework import routers
from .api import KernelViewSet, ProjectSummaryViewSet

router = routers.DefaultRouter()
router.register('api/kernel', KernelViewSet, "kernel")
router.register('api/user_projects', ProjectSummaryViewSet, "user_projects")
#router.register('api/test', testViewSet, 'test')
urlpatterns = router.urls