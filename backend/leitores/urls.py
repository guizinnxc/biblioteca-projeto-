from rest_framework.routers import SimpleRouter

from .views import LeitorViewSet

router = SimpleRouter()
router.register('leitores', LeitorViewSet)

urlpatterns = router.urls
