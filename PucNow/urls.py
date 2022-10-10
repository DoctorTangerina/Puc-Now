"""PucNow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PucNowapp import views
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('',views.PaginaInicial,name='login'),
    path('esquecido/',views.EsqueceuSenha,name='esqueci'),
    path('cadastro/',views.Cadastro,name='cadastro'),
    path('perfil/',views.Perfil,name='perfil'),
    path('home/',views.Home,name='home'),
    path('cria-grupo/',views.CriaGrupo,name='cria-grupo'),
    path('pesquisa-grupo/',views.PesquisaGrupo,name='pesquisa-grupo'),
    path('grupo-de-estudos/',views.GrupoEstudos,name='grupo-de-estudos')
]

