from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^centrocosto/(?P<pk>[0-9]+)$', views.CENTROCOSTO_GPD),
    url(r'^centrocosto/', views.CENTROCOSTO_GP),
    url(r'^mediopago/(?P<pk>[0-9]+)$', views.MEDIOPAGO_GPD),
    url(r'^mediopago/', views.MEDIOPAGO_GP),
    url(r'^tipocomprobante/(?P<pk>[0-9]+)$', views.TIPOCOMPROBANTE_GPD),
    url(r'^tipocomprobante/', views.TIPOCOMPROBANTE_GP),
]