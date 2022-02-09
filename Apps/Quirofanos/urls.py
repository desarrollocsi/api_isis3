from django.urls import path, include
from django.conf.urls import url
#
from .anestesia.views import *
from .intervencion.views import *
from .salas.views import *
from .programacion.views import *
from .personales.views import *
from .participantes.views import *



urlpatterns = [
    url(r'^anestesia', anestesia_api_view),
    url(r'^personales', personales_api_view),
    url(r'^programaciones', programaciones_api_view),
    url(r'^salas',salas_api_view),
    url(r'^intervencion/(?P<pk>\d+)/$', intervencion_api_view),
    url(r'^intervencionporcodigo/(?P<pk>\d+)/$', intervencion_codigo_api_view),
    url(r'^programacion/(?P<pk>\d+)/$',programacion_detalle_api_view),
    # url(r'^participantes/(?P<pk>\d+)/$',participantes_api_view),

    # url(r'^programacionview/(?P<pk>\d+)/$',programacion_view),
    # path('disponibilidadsalas/<str:sala>/<str:fecha>',disponibilidad_salas_api_view)
    # path('agendasoap/<str:pk>',soap_api_view)
]
