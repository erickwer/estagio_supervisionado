from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Pessoa)

admin.site.register(Professor)

admin.site.register(Banca)

admin.site.register(Aluno)

admin.site.register(Projeto)
