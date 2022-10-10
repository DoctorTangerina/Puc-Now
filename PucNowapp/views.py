from django.shortcuts import render
from django.http import HttpResponse,request

def PaginaInicial(request):
    return render(request,'login.html')



