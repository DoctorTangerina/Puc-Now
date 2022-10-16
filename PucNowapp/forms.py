from django import forms

class Cadastrar(forms.Form):
    token = forms.CharField(max_length=100)
    name = forms.CharField(max_length=40)
    username = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    password = forms.CharField(max_length=40)
    course = forms.CharField(max_length=30)
    semester = forms.IntegerField()