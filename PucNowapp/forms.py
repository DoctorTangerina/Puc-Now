from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class Cadastrar(forms.Form):

    name = forms.CharField(label=False, max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    username = forms.CharField(label=False, max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário'}))
    email = forms.EmailField(label=False, max_length=40, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label=False, max_length=40, widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    course = forms.CharField(label=False, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Curso'}))
    semester = forms.IntegerField(label=False, widget=forms.NumberInput(attrs={'placeholder': 'Período'}))
    
    def clean_email(self):
        emil = self.cleaned_data['email']
        if Student.objects.filter(email = emil).exists():
            raise ValidationError('email ja esta em uso'.format(emil))

        return emil

    def clean_username(self):
        nombre = self.cleaned_data['username']
        if Student.objects.filter(username = nombre).exists():
            raise ValidationError('esse nome ja esta em uso'.format(nombre))

        return nombre

class Login(forms.Form):
    username = forms.CharField(label=False, max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário'}))
    password = forms.CharField(label=False, max_length=40, widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))    
    
    def clean_username(self):
        nome = self.cleaned_data['username']
        if not Student.objects.filter(username = nome).exists():
            raise ValidationError('Usuário não existe'.format(nome))

        return nome
        
    def clean_password(self):
        if self.errors:
            return None
            
        nome = self.cleaned_data['username']
        user = Student.objects.filter(username = nome)
        
        senha = self.cleaned_data['password']
        if not user.values()[0]['password'] == senha:
            raise ValidationError('Senha incorreta')
            
        return senha
