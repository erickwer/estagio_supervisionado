from django.urls import path
from .views import *


urlpatterns = [
  path('', retornaMeusAlunos, name="vw_orientador"),
  path('addProjeto/<int:id>', addProjeto, name="addProjeto"),
  path('update/<int:id>', updateProjeto, name="update"),
  path('meusAlunos/', retornaOrientadorAluno, name="retornaOrientadorAcademico"),


]