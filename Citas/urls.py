from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from Citas import views

# router = DefaultRouter()
# router.register(r'especialidades', views.EspecialidadViewSet)
# router.register(r'medicos', views.MedicosViewSet)
# router.register(r'turnos', views.TurnosViewSet)
# router.register(r'consultorios', views.ConsultoriosViewSet)
# router.register(r'programaciones', views.ProgramacionViewSet)
# urlpatterns = router.urls

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

    url('medicosespecialidad', views.MedicosList.as_view()),
    url('programacionesfecha', views.ProgramacionList.as_view()),
    url(r'^prueba$', views.pruebas),
]


# from AppCitas import views
# urlpatterns = [ 
#     url(r'^api/citas/(?P<pk>[0-9]+)$', views.citas_paciente),
#     url(r'^api/consultas$', views.datos_dni),
#     url(r'^api/consulta/(?P<dni>[0-9]+)$', views.consultacitas),
#     url(r'^ /(?P<fecha>[0-9]+)$', views.consulta_programacion),
#     url(r'^api/prueba$', views.pruebas),
#     #url(r'^api/consultas$', '91209906'),
# ]
