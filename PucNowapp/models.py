from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    course = models.CharField(max_length=30)
    semester = models.PositiveSmallIntegerField()

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

class Friends1(models.Model):
    users1=models.ManyToManyField(Student,null=True)
    current_user=models.ForeignKey(Student,related_name='owner',on_delete=models.CASCADE,null=True)



    @classmethod
    def make_friend(cls,current_user,new_friend):
        friend,create=cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users1.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, create = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users1.remove(new_friend)