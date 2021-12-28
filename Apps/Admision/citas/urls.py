from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from Apps.Admision.citas.agendamedica import views as agendaviews
from Apps.Admision.citas.programacion import views as programacionviews
# Lsita URL Citas .
urlpatterns = [
    ## ----------------------------------------------------------------------
    ## ----------------     URL AGENDA MEDICA      -------------------------
    ## ----------------------------------------------------------------------
    # 1.- Acto Médico Listar :
    url('medicosespecialidad', agendaviews.MedicosList.as_view()), #Parametros => "especialidad"=005
    url('pacientescitados', agendaviews.CitasList.as_view()),
    url('cie10', agendaviews.Cie10List.as_view()),
    ## --------------------------------------------------------
    #------------------ CRUD  ACTO MEDICO     -----------------
    # ---------------------------------------------------------
    url(r'^actomedico/(?P<pk>[0-9]+)$', agendaviews.ACTOMEDICO_GPD),
    url(r'^actomedico', agendaviews.REGISTRE_ACTOMEDICO),

    # 1.- Agenda Medica :
    url('especialidadesprogramacion', agendaviews.EspeciliadadProgramacionList.as_view()), # Parametros => "fecha"=20200101&"especialidad"=005
    url('medicosprogramacion', agendaviews.MedicosProgramacionList.as_view()), # Parametros => "fecha" = 20200101
    url('agendamedica', agendaviews.AgendaMedicaListView.as_view()), # Parametros => "programacion" = 00059771
    url('planeshistoria', agendaviews.IafasListView.as_view()),  # Parametros => "historia"=0000055579

    url(r'^citas/(?P<pk>[0-9]+)$', agendaviews.CITAS_GPD),
    url(r'^citas', agendaviews.CITAS_GP),

    ## ----------------------------------------------------------------------
    ## ----------------     URL PROGRAMACIONES      -------------------------
    ## ----------------------------------------------------------------------
    url(r'^programaciones/(?P<pk>[0-9]+)$', programacionviews.PROGRAMACION_GPD),
    url(r'^programaciones', programacionviews.PROGRAMACION_GP),
    url('programacionesfecha', programacionviews.ProgramacionList.as_view()),

]