from rest_framework.routers import DefaultRouter

from api.views import ProviderListViewSet

app_name = "api"
router = DefaultRouter()
router.register(r'providers', ProviderListViewSet, basename='provider')

urlpatterns = router.urls
