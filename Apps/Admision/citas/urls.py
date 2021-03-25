from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from Apps.Admision.citas import views
# Lsita URL Citas .
urlpatterns = [
    url('medicosespecialidad', views.MedicosList.as_view()),
    url('programacionesfecha', views.ProgramacionList.as_view()),    
    url('pacientescitados', views.CitasList.as_view()), 
    url('cie10', views.Cie10List.as_view()), 
    url('antecedentes', views.AntecedentesList.as_view()), 
    url(r'^programaciones/(?P<pk>[0-9]+)$', views.PROGRAMACION_GPD),
    url(r'^programaciones', views.PROGRAMACION_GP),
    url(r'^actomedico', views.REGISTRE_ACTOMEDICO),
]