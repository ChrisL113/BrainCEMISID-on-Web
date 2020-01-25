from rest_framework import routers
from .api import ImageSettingsSetViewSet, ProjectImageSettings



router = routers.DefaultRouter()
router.register('api/images_settings_set', ImageSettingsSetViewSet, 'images_settings_set')
router.register('api/project_image_settings', ProjectImageSettings, 'project_image_settings')

urlpatterns = router.urls