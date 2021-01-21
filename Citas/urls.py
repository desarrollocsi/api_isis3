from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from Citas import views

# from .views import EspecialidadViewSet,MedicosViewSet
# from .models import Especialidades,Medicos

router = DefaultRouter()
router.register(r'especialidades', views.EspecialidadViewSet)
router.register(r'medicos', views.MedicosViewSet)
router.register(r'turnos', views.TurnosViewSet)
router.register(r'consultorios', views.ConsultoriosViewSet)
# router.register(r'programaciones', views.ProgramacionViewSet)
urlpatterns = router.urls
urlpatterns += [ 
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
