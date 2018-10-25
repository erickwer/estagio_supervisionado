from django.urls import path
from . import views

urlpatterns = [
    path('', views.coordenador, name='vw_coordenador'),
    path('orientadorAcademico/', views.OrientadorAcademico, name='orientadorAcademico')
]