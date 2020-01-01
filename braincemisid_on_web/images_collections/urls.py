from rest_framework import routers
from .api import AllCollectionsViewSet,UserCollectionViewSet 

router = routers.DefaultRouter()
router.register('api/user_collection', UserCollectionViewSet, 'user_collection')
router.register('api/all_collections', AllCollectionsViewSet,'all_collections')
urlpatterns = router.urls