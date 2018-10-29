from django.db import models


# Create your models here.


class Pessoa(models.Model):
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    nome = models.CharField(max_length=255)
    data_de_nascimento = models.DateField(null=True, blank=True)
    rg = models.CharField(max_length=32, blank=True, null=True, verbose_name='RG')
    cpf = models.CharField(max_length=14, null=True, blank=True, verbose_name='CPF')
    endereco = models.CharField(max_length=255, null=True, blank=True, verbose_name='Endereço')
    cidade = models.CharField(max_length=128, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True, verbose_name='CEP')
    bairro = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, verbose_name='E-mail')
    telefone_residencial = models.CharField(max_length=32, null=True, blank=True)
    telefone_celular = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

    professor = models.OneToOneField(Pessoa, on_delete=models.CASCADE, null=True)
    matricula_funcional = models.IntegerField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.professor.nome


class Aluno(models.Model):
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    aluno = models.OneToOneField(Pessoa, on_delete=models.SET_NULL, null=True)
    cgu = models.IntegerField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.aluno.nome

# Classe que vincula o aluno a um professor (Orientador)
class OrientadorAcademico(models.Model):
    class Meta:
        verbose_name= 'OrientadorAcademico'
        verbose_name_plural ='OrientadorAcademico'
    status = models.CharField(null=True, max_length=200)
    professor = models.ForeignKey(Professor,  on_delete=models.SET_NULL, null=True)
    aluno = models.OneToOneField(Aluno, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.professor.professor.nome, self.aluno.aluno.nome)


# Classe que define a estrutura do projeto de TCC ou ESTAGIO
class Projeto(models.Model):
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
    tcc = 1
    estagio = 2
    choices = (
        (tcc, ('TCC')),
        (estagio, ('ESTÁGIO'))
    )
    identificador = models.IntegerField(max_length=200, null=True, choices=choices, default=tcc)
    periodo = models.CharField(max_length=200, null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    titulo = models.CharField(max_length=500,  blank=True)
    vinculo = models.OneToOneField(OrientadorAcademico, on_delete=models.CASCADE, null=False, blank=False)
    professoresBanca = models.ManyToManyField(Professor, null=True, blank=True)
    notaFinal = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.titulo


