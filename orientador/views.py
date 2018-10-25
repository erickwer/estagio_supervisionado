from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from disciplina.views import *
from disciplina.forms import *
# Create your views here.

def orientador(request):
    return render(request, 'vw_orientador.html')

def retornaOrientadorAluno (request):
    relacoes = OrientadorAcademico.objects.all()
    return render(request, 'vw_alunosOrientador.html', {'relacoes': relacoes})


def retornaMeusAlunos(request):
    projMeusAlunos = Projeto.objects.filter(vinculo__professor__professor_id=2)
    return  render(request, 'vw_orientador.html', {'projMeusAlunos': projMeusAlunos})

def addProjeto(request, id ):
    vinculo =get_object_or_404(OrientadorAcademico, pk=id)
    form = ProjetoForm(request.POST or None, instance=vinculo)
    form.vinculo = vinculo
    if form.is_valid():
        form.save()
        return redirect('vw_projetos')
    return render(request, 'projeto_form.html', {'form': form})


def updateProjeto(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    form = ProjetoForm(request.POST or None, instance=projeto)
    if form.is_valid():
        form.save()
        return  redirect('vw_projetos')
    return render(request, 'projeto_form.html', {'form':form})



def teste(request):
    return HttpResponse("Imprimeeeeeeeeee")