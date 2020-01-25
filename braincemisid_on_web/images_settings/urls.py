from rest_framework import routers
from .api import ImageSettingsSetViewSet



router = routers.DefaultRouter()
router.register('api/images_settings_set', ImageSettingsSetViewSet, 'images_settings_set')
#router.register('api/user_category/(?P<category>\d+)/?$', UserFilterImageViewSet, "user_category")

urlpatterns = router.urls