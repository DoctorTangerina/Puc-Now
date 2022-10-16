from django import forms

class Cadastrar(forms.Form):
    name = forms.CharField(label=False, max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    username = forms.CharField(label=False, max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário'}))
    email = forms.EmailField(label=False, max_length=40, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label=False, max_length=40, widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    course = forms.CharField(label=False, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Curso'}))
    semester = forms.IntegerField(label=False, widget=forms.NumberInput(attrs={'placeholder': 'Período'}))