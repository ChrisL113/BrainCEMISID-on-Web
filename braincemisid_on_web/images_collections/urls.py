from rest_framework import routers
from .api import AllCollectionsViewSet,UserCollectionViewSet 
from django.conf.urls.static import static
from django.conf import settings



router = routers.DefaultRouter()
router.register('api/user_collection', UserCollectionViewSet, 'user_collection')
router.register('api/all_collections', AllCollectionsViewSet,'all_collections')

urlpatterns = router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)