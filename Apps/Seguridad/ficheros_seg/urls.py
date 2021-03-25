from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from Apps.Seguridad.ficheros_seg import views

router = DefaultRouter()
router.register(r'roles', views.rolsViewSet)
urlpatterns = router.urls