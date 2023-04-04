from api.views import ProviderListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'providers', ProviderListViewSet, basename='provider')

urlpatterns = router.urls
