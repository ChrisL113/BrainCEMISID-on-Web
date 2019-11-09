from rest_framework import routers
from .api import ProjectViewset

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewset, "projects")
urlpatterns = router.urls