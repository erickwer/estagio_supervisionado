from django.urls import path
from . import views

urlpatterns = [
 path('', views.projetos, name='vw_projetos'),
 path('estagio/', views.estagio, name='vw_estagio'),
 path('tcc/', views.tcc, name='vw_tcc'),

]