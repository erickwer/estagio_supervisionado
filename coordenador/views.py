from django.shortcuts import render, redirect
from disciplina.forms import OrientadorAcademicoForm
# Create your views here.
def coordenador (request):
    return  render(request, 'vw_coordenador.html')

def OrientadorAcademico(request):
    if request.method =="POST":
        form = OrientadorAcademicoForm(request.POST)
        if form.is_valid():
            orientaAcad = form.save(commit=False)
            orientaAcad.status = "Vinculado"
            orientaAcad.save()
            return redirect('vw_coordenador')
    else:
        form = OrientadorAcademicoForm()
        return render(request, 'orientadorAcademicoForm.html', {'form': form})


    # form = OrientadorAcademicoForm(request.POST or None)
    #
    # if form.is_valid():
    #     form.status = 'Vinculado'
    #     form.save()
    #     return redirect('vw_coordenador')
    # return render(request, 'orientadorAcademicoForm.html', {'form': form})
