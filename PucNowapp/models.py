from django.db import models

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    semester = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=40)
    
    

    
