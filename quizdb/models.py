from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class user1(models.Model):
    #username=models.CharField(max_length=25,primary_key=True)
    #email_id=models.CharField(max_length=25)
    #password=models.CharField(max_length=10)
    contact_no=models.IntegerField()
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    def setAttribute(self,phone_no,address,age,user_id):
        self.contact_no=phone_no
        self.address=address
        self.user_id=user_id
        self.age=age

class questions(models.Model):
    question_id=models.AutoField(primary_key=True)
    question=models.CharField(max_length=140)
    option1=models.CharField(max_length=100,default='SOME STRING')
    option2=models.CharField(max_length=100,default='SOME STRING')
    option3=models.CharField(max_length=100,default='SOME STRING')
    option4=models.CharField(max_length=100,default='SOME STRING')
    correct_answer=models.CharField(max_length=1)
    solution=models.CharField(max_length=210)

class quiz(models.Model):
    quiz_id=models.IntegerField(primary_key=True)
    quiz_name=models.CharField(max_length=10)
    duration=models.IntegerField()

class feedback(models.Model):
    question_id=models.IntegerField(primary_key=True)
    feedback=models.CharField(max_length=100)
class teacher_questions(models.Model):
    question_id=models.AutoField(primary_key=True)
    question=models.CharField(max_length=140)
    option1=models.CharField(max_length=100,default='SOME STRING')
    option2=models.CharField(max_length=100,default='SOME STRING')
    option3=models.CharField(max_length=100,default='SOME STRING')
    option4=models.CharField(max_length=100,default='SOME STRING')
    correct_answer=models.CharField(max_length=1)
    solution=models.CharField(max_length=210)
    quiz_id=models.IntegerField()

