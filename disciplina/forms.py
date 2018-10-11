from django.forms import ModelForm
from .models import Projeto

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = ['identificador', 'titulo', 'autor','orientador','banca']