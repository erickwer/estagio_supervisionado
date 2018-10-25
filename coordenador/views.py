from django.shortcuts import render, redirect
from disciplina.forms import OrientadorAcademicoForm
# Create your views here.
def coordenador (request):
    return  render(request, 'vw_coordenador.html')

def OrientadorAcademico(request):
    form = OrientadorAcademicoForm(request.POST, None)
    if form.is_valid():
        form.save()
        return redirect('vw_coordenador')
    return render(request, 'orientadorAcademicoForm.html', {'form': form})