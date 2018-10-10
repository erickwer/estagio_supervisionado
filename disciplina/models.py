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


class Banca(models.Model):
    class Meta:
        verbose_name = 'Banca'
        verbose_name_plural = 'Bancas'

    identificacao = models.CharField(max_length=500)
    professores = models.ManyToManyField(Professor)

    def __str__(self):
        return self.identificacao


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
    identificador = models.IntegerField(max_length=200, null=True,choices=choices, default=tcc)
    titulo = models.CharField(max_length=500)
    autor = models.OneToOneField(Aluno, on_delete=models.SET_NULL, null=True)
    orientador = models.OneToOneField(Professor, on_delete=models.SET_NULL, null=True)
    banca = models.OneToOneField(Banca, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo




