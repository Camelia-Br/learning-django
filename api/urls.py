from rest_framework.routers import DefaultRouter

from api.views import ProviderListViewSet

router = DefaultRouter()
router.register(r'providers', ProviderListViewSet, basename='provider')

urlpatterns = router.urls
