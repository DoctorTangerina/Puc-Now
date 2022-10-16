from django.shortcuts import render
from django.http import HttpResponse,request
from .models import Student
from .forms import Cadastrar

def PaginaInicial(request):
    return render(request,'Login.html')

def EsqueceuSenha(request):
    return render(request,'Esqueci.html')

def Cadastro(request):
    if request.method == 'POST':
        form = Cadastrar(request.POST)
        print(request.POST)
        if(form.is_valid()):
            Student(form[1:]).save()
            print("cheguei aq")
            return render(request,'Login.html')
    return render(request,'Cadastro.html')

def Perfil(request):
    return render(request,'Perfil.html')

def Home(request):
    return render(request,'Home.html')

def CriaGrupo(request):
    return render(request,'CriaGrupo.html')

def PesquisaGrupo(request):
    return render(request,'PesquisaGrupo.html')

def GrupoEstudos(request):
    return render(request,'GrupoEstudos.html')



