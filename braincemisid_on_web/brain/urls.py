from rest_framework import routers
from .api import KernelViewSet, ProjectSummaryViewSet, DesiredStateViewset

router = routers.DefaultRouter()
router.register('api/kernel', KernelViewSet, "kernel")
router.register('api/user_projects', ProjectSummaryViewSet, "user_projects")
router.register('api/desired_state', DesiredStateViewset, "desired_state")
#router.register('api/test', testViewSet, 'test')
urlpatterns = router.urls