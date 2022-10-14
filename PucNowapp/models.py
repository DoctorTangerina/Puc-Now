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

class StudyGroup(models.Model):
    groupId = models.PositiveIntegerField()
    private = models.BooleanField()

class Event(models.Model):
    groupId = models.PositiveIntegerField()
    local = models.CharField(max_length=20)
    time = models.TimeField()
    weekday = models.CharField(max_length=20)

class PrivateChat(models.Model):
    chatId = models.PositiveIntegerField()
    userId1 = models.PositiveIntegerField()
    userId2 = models.PositiveIntegerField()

class GroupChat(models.Model):
    chatId = models.PositiveIntegerField()
    groupId = models.PositiveIntegerField()
    
class Message(models.Model):
    chatId = models.PositiveIntegerField()
    groupId = models.PositiveIntegerField()
    content = models.CharField(max_length=32767)
    owner = models.CharField(max_length=20)
    dateTimeSent = models.DateTimeField()
    sent = models.BooleanField()
