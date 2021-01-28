from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from formulario import views

router = DefaultRouter()
router.register(r'formulario', views.formularioViewSet)
router.register(r'formularioc', views.formulariocViewSet)
urlpatterns = router.urls