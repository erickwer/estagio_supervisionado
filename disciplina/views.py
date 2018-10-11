from django.shortcuts import render, redirect
from .forms import ProjetoForm
from django.http import HttpResponse
# Create your views here.
from .models import *

def projetos(request):
    return render(request, 'vw_projeto.html')

def estagio(request):
    estagios = Projeto.objects.filter(identificador=2)
    return render(request, 'vw_estagios.html', {'estagios': estagios})

def tcc(request):
    tccs = Projeto.objects.filter(identificador=1)
    return render(request, 'vw_tccs.html', {'tccs': tccs})


def add_projeto(request):
    form = ProjetoForm(request.POST, None)
    if form.is_valid():
        form.save()
        return redirect('vw_projetos')
    return render(request, 'projeto_form.html', {'form': form} )