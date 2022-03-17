from django.conf.urls import url
from Apps.Unilabs import views

# Lsita URL Unilabs .
urlpatterns = [
    url('consultaexamenes', views.UnilabsView.as_view()),
]