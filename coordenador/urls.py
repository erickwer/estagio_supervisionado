from django.urls import path

from . import views

urlpatterns = [
    path('', views.coordenador, name='vw_coordenador')
]