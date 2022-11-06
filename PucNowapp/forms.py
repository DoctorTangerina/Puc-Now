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
            raise ValidationError ('email ja esta em uso'.format(emil))

        return emil

    def clean_usernome(self):
        nombre = self.cleaned_data['username']
        if Student.objects.filter(username = nombre).exists():
            raise ValidationError ('esse nome ja esta em uso'.format(nombre))

        return nombre