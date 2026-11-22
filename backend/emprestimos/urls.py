from rest_framework.routers import SimpleRouter

from .views import EmprestimoViewSet

router = SimpleRouter()
router.register('emprestimos', EmprestimoViewSet)

urlpatterns = router.urls
