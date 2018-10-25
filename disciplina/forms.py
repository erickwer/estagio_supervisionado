from django.forms import ModelForm
from django import forms
from .models import Projeto, OrientadorAcademico


class ProjetoForm(ModelForm):

    class Meta:
        model = Projeto
        exclude = ['periodo', 'notaFinal', 'vinculo']
        labels = {
            'identificador':'Identificador',
            'data': 'Data',
            'titulo':'Titulo',
            'professoresBanca': 'Professores na Banca',
            }

        widgets={
            'data': forms.DateInput(format='%d/%m/%y')
        }


class OrientadorAcademicoForm(ModelForm):

    class Meta:
        model = OrientadorAcademico
        fields =['aluno','professor']