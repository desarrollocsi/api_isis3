from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from Apps.Admision.ficheros import views
# from ficheros import views


urlpatterns = [
    #----------------------------------------------------------------------------
    #---  URL : CRUD . JLT :2021/01/22 - Se definio los crud automatizados.  ----
    # --  Las vistas se encuentra con los prefijos : 'GPD' => 'GET','PUT','DELETE'
    #                                                 'GP' => 'GET', 'POST'
    # ---------------------------------------------------------------------------
    url(r'^especialidades/(?P<pk>[0-9]+)$', views.ESPECIALIDADES_GPD),
    url(r'^especialidades/', views.ESPECIALIDADES_GP),
    url(r'^medicos/(?P<pk>[0-9]+)$', views.MEDICOS_GPD),
    url(r'^medicos/', views.MEDICOS_GP),
    url(r'^turnos/(?P<pk>[0-9]+)$', views.TURNOS_GPD),
    url(r'^turnos/', views.TURNOS_GP),
    url(r'^consultorios/(?P<pk>[0-9]+)$', views.CONSULTORIOS_GPD),
    url(r'^consultorios/', views.CONSULTORIOS_GP),

    url(r'^paises/(?P<pk>[0-9]+)$', views.PAISES_GPD),
    url(r'^paises/', views.PAISES_GP),
    url(r'^estadosciviles/(?P<pk>[0-9]+)$', views.ESTADOSCIVILES_GPD),
    url(r'^estadosciviles/', views.ESTADOSCIVILES_GP),
    url(r'^tipodedocumentos/(?P<pk>[0-9]+)$', views.TIPOSDEDOCUMENTOS_GPD),
    url(r'^tipodedocumentos/', views.TIPOSDEDOCUMENTOS_GP),
    url(r'^ocupaciones/(?P<pk>[0-9]+)$', views.OCUPACIONES_GPD),
    url(r'^ocupaciones/', views.OCUPACIONES_GP),


    url('antecedentes', views.AntecedentesList.as_view()),

    # url(r'^prueba$', views.pruebas),
]