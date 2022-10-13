from django.shortcuts import render
from django.http import HttpResponse,request

def PaginaInicial(request):
    return render(request,'login.html')

def EsqueceuSenha(request):
    return render(request,'esqueci.html')

def Cadastro(request):
    return render(request,'Cadastro.html')

def Perfil(request):
    return render(request,'Perfil.html')

def Home(request):
    return render(request,'home.html')

def CriaGrupo(request):
    return render(request,'CriaGrupo.html')

def PesquisaGrupo(request):
    return render(request,'PesquisaGrupo.html')

def GrupoEstudos(request):
    return render(request,'GrupoEstudos.html')



