from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
#import pymysql
from quizdb.models import user1
from django.views import generic
from django.template.context_processors import csrf
from quizdb.models import questions
from quizdb.models import quiz
from quizdb.models import teacher_questions

# Create your views here..

class StudentListView(generic.ListView):
    model = user1

#def addquestion(request):
 #   c = {}
  #  c.update(csrf(request))
   # return render(request,'addquestion.html', c)


def getusername_del(request):
    c = {}
    c.update(csrf(request))
    return render(request,'delete_student.html', c)
def getusername_update(request):
    c = {}
    c.update(csrf(request))
    return render(request,'update_username.html', c)

   
def addstudentinfo(request):
    if request.method=="POST":
        user = User.objects.create_user(username=request.POST.get('user_name'), password=request.POST.get('password'), email=request.POST.get('email'))
        newUser = user1()
        newUser.setAttribute(request.POST.get('contact_no'),request.POST.get('address'),request.POST.get('age'),user.id)
        newUser.save()
        user.save()
        auth.login(request,user)
        return render(request,'addrecord.html')
    else:
        return render(request,'addstudentinfo.html')

    
def viewinfo(request):
     users=user1.objects.all()
     
     return render(request,'user_list.html',{'users':users})
def updateinfo(request):
    user_name = request.POST.get('user_name', '')
    student = user1.objects.filter(username = user_name)
    if not student :
        return HttpResponseRedirect('/quizdb/delunsuccess/')
    else:
        for s in student:
            s.delete()
        return  render(request,'getinfo_update.html')
def delunsuccess(request):
    return render(request,'notfound.html')
def delstudentinfo(request):
    user_name = request.POST.get('user_name', '')
    student = user1.objects.filter(username = user_name)
    if not student :
        return HttpResponseRedirect('/quizdb/delunsuccess/')
    else:
        for s in student:
            s.delete()
        return  render(request,'delrecord.html')
def addquestioninfo(request):
     question = request.POST.get('question', '')
     option1 = request.POST.get('option1', '')
     option2 = request.POST.get('option2', '')
     option3 = request.POST.get('option3', '')
     option4 = request.POST.get('option4', '')
     correct_answer = request.POST.get('correct_answer', '')
     solution = request.POST.get('solution', '')
     question_full=questions(question=question,option1=option1,option2=option2,option3=option3,option4=option4,correct_answer=correct_answer,solution=solution)
     question_full.save()
     question = request.POST.get('add_question', '')
     if not question:
        return render(request,'Quiz_success.html')
     else:
        return render(request,'addquestion.html')
     
    

def addteacher_questioninfo(request):
        question = request.POST.get('question', '')
        option1 = request.POST.get('option1', '')
        option2 = request.POST.get('option2', '')
        option3 = request.POST.get('option3', '')
        option4 = request.POST.get('option4', '')
        correct_answer = request.POST.get('correct_answer', '')
        solution = request.POST.get('solution', '')
        quizid = request.POST.get('quiz_id')
        print(quizid)
        questions=teacher_questions(question=question,option1=option1,option2=option2,option3=option3,option4=option4,correct_answer=correct_answer,solution=solution,quiz_id=quizid)
        questions.save()
        question = request.POST.get('add_question', '')
        if not question:
            return render(request,'Quiz_success.html')
        else:
            return render(request,'addteacher_questioninfo.html')
def add_quiz(request):
    if request.method== "POST":
        quiz_name = request.POST.get('quiz_name', '')
        duration = request.POST.get('duration', '')
        quiz_id = request.POST.get('quiz_id', '')
        quiz_object=quiz(quiz_name=quiz_name,duration=duration,quiz_id=quiz_id)
        quiz_object.save()
        if request.session.get('quiz_id'):pass
        else:
            request.session['quiz_id']=quiz_id
       # return render(request,'addteacher_questioninfo.html')
        return HttpResponseRedirect('/quizdb/addteacher_questioninfo')
    else:
        print("123")
        return render(request,'add_quiz.html')
def give_quiz(request):
    questions1=questions.objects.all()
    return render(request,'give_quiz.html',{'questions1':questions1})

def validate_answer(request):
    selectedOptions=[]
    correctAnswers=[]
    if request.method=="POST":
        questions1=questions.objects.all()
        for question in questions1:
            selectedOptions.append(request.POST.get('question' + str(question.question_id),''))
            correctAnswers.append(question.correct_answer)
        
            
    mylist=zip(selectedOptions,correctAnswers)
    return render(request,'validate_answer.html',{'mylist':mylist})    
        
