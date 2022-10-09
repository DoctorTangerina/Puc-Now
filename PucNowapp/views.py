from django.shortcuts import render
from django.http import HttpResponse,request

def op(request):
    render(request,'login.css')
    return render(request,'login.html')


