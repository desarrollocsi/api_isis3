from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from formulario import views

router = DefaultRouter()
router.register(r'formulario', views.formulariocViewSet)
urlpatterns = router.urls