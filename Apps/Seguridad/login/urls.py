from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from Apps.Seguridad.login.views import LoginAPI

# Lsita URL Login .
urlpatterns = [
    url('login', LoginAPI.as_view(),name='login'),
    # url('logout', LogoutAPI.as_view(),name='logout'),
]


