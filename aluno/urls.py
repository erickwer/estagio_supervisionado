from django.urls import path

from . import views

urlpatterns = [
path('', views.aluno, name='vw_aluno')
]