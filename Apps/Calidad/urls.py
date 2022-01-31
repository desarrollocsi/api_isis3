from django.urls import path, include
from django.conf.urls import url
#
from .views import *

urlpatterns = [    
    url(r'^involucrados',involucrados_iea_api_view),
    url(r'^incidencia/(?P<pk>\d+)/$', incidencia_detail_api_view),
    url(r'^incidenciachancestatus/(?P<pk>\d+)/$', incidencia_chance_status),
    path('incidencias/<str:fecha>/<str:rol>',incidencia_api_view),
    url(r'^incidencias',incidencia_api_register)
]