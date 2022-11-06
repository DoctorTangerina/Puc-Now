from django.shortcuts import render
from django.http import HttpResponse,request
from .models import Student
from .forms import Cadastrar, Login
from django.core.mail import send_mail

def ValidaEmail(request):
    form = Cadastrar(request.POST)
    if(form.is_valid()):
        Student(name=request.POST['name'], username=request.POST['username'], password=request.POST['password'], email=request.POST['email'], 
        course=request.POST['course'], semester=request.POST['semester']).save()
        return render(request,'Validando.html')
    return render (request, 'Validando.html')

def PaginaInicial(request):
    if request.method == 'POST':
        log = Login(request.POST)
        if(log.is_valid()):
            return Home(request)
    else:
        log = Login() 
    return render(request,'Login.html', {'form': log})

def EsqueceuSenha(request):
    return render(request,'Esqueci.html')

def Cadastro(request):
    if request.method == 'POST':
        form = Cadastrar(request.POST)
        if(form.is_valid()):
            send_mail('validacao de email','por favor valide seu email clicando nesse link: ','from@example.com',['to@example.com'],fail_silently=False)
            return ValidaEmail(request)
    else:
        form = Cadastrar()
    return render(request,'Cadastro.html', {'form': form})

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

def Config(request):
    return render(request,'Configuracao.html')



