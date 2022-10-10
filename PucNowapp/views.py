from django.shortcuts import render
from django.http import HttpResponse,request

def op(request):
    return render(request,'login.html')


