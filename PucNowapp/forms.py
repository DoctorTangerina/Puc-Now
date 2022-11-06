from django import forms
from django.contrib.auth.models import User
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
        email = self.cleaned_data['Email']
        if User.objects.filter(Email = email).exists():
            raise ValidationError ('email ja esta em uso'.format(email))

        return email