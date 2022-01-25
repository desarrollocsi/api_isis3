from django.conf.urls import url
from Apps.Reclamos import views

# Lsita URL Citas .
urlpatterns = [
    url('estado', views.EstadoList.as_view()),
    url('etapa', views.EtapaList.as_view()), 
    url('resultado', views.ResultadoList.as_view()), 
    url('tipodocumento', views.TipoDocumetoList.as_view()), 
    url('clasificacion', views.ClasificacionList.as_view()), 
    url('servicio', views.ServicioList.as_view()), 
    url('mediorecepcion', views.MedioList.as_view()),
    url('motconcant', views.MotConcAntList.as_view()), 
    url(r'^reclamos/(?P<pk>[0-9]+)$', views.RECLAMO_GPPD),
    url('reclamos/lista', views.ReclamosList.as_view()),
    url(r'^tramas/(?P<_periodo>[0-9]+)$', views.TRAMAS_GP),
]