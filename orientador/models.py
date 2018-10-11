from django.db import models
from disciplina.views import Professor
class Orientador(models.Model):
    class Meta:
        verbose_name='Orientador'
        verbose_name_plural='Orientadores'

    orientador = models.OneToOneField(Professor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.orientador.professor.nome