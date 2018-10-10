from django.shortcuts import render

# Create your views here.
def coordenador (request):
    return  render(request, 'vw_coordenador.html')