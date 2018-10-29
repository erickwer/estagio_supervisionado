from django.forms import ModelForm, models, HiddenInput
from django import forms
from .models import Projeto, OrientadorAcademico


class ProjetoForm(ModelForm):
    # vinculo = forms.ModelChoiceField(label='OrientadorAcademico', widget=forms.Select(attrs={'readonly': 'readonly'}),
    #                                 queryset=OrientadorAcademico.objects.none())
    # def __init__(self, *args, **kwargs):
    #     super(ProjetoForm, self).__init__(*args, **kwargs)
    #     self.fields['vinculo'].queryset = OrientadorAcademico.objects.filter(pk=kwargs.get('initial').get('orientadorAcademico').pk)
    #     self.fields['vinculo'].widget = HiddenInput()

    class Meta:
        model = Projeto
        fields = ('identificador', 'data','titulo', 'professoresBanca')

        widgets={
            'data': forms.DateInput(format='%d/%m/%y')
        }


class OrientadorAcademicoForm(ModelForm):

    class Meta:
        model = OrientadorAcademico
        fields =['aluno','professor']
    #
    # def clean(self):
    #     aluno = self.cleaned_data['aluno']
    #     if OrientadorAcademico.objects.filter(aluno__aluno__nome=aluno).exists():
    #         print("dentro da func")
    #         raise forms.ValidationError(
    #             "Este aluno já está vinculado a um orientador!", aluno.aluno.nome
    #         )
