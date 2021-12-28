from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.urls import path

from Apps.Admision.pacientes.historias import views as histoiasviews
from Apps.Admision.pacientes.atenciones import views as atencionesviews
from .atenciones.views import AtencionesListView
# Lsita URL Citas .
urlpatterns = [
    # --------------------------------------------------------------------
    # ------------------------  HISTORIAS       ----------------------------
    # --------------------------------------------------------------------
    url('historiasbuscar', histoiasviews.HistoriasSearchList.as_view()), 
    url(r'^historias/(?P<pk>[0-9]+)$', histoiasviews.HISTORIAS_GPD),
    url(r'^historias/', histoiasviews.HISTORIAS_GP),

    url(r'^listaratenciones/(?P<id>\w+)$', atencionesviews.consultacitas),
    # url(r'^atenciones', atencionesviews.AtencionesListView), 
    url('lisatenciones',atencionesviews.AtencionesListView.as_view(),),
]