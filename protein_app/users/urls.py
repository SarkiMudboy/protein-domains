from views import ResearcherViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('researchers', ResearcherViewSet, basename='researcher')

urlpatterns = router.urls