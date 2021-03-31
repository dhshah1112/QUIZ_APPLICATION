from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from quizdb.models import questions

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request,'login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username,password=password)
    if username == "admin" and password == "admin123":
            return admin(request)
    if user is not None:
        auth.login(request, user)
        return  loggedin(request)
    else:
        return invalidlogin(request)

def loggedin(request):
    return render(request,'index.html')

def invalidlogin(request):
    return render(request,'invalidlogin.html')

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')
def admin(request):
    if request.method=="POST":
        questions1=questions.objects.all()
        return render(request,'admin.html',{'questions1':questions1})
    else:
        return render(request,'admin.html')
     
def modify(request):
    id=request.POST.get('question_id')
    question=questions.objects.filter(question_id=id)
    
    return render(request,'modify.html',{'question':question})
class registration(TemplateView):
    template_name='loginmodule/registration.html' 

def modified(request):
    id=request.POST.get('question_id')
    
    selectquestion=questions.objects.filter(question_id=id)
    
    selectquestion.delete()
    questions1=questions.objects.all()
    question = request.POST.get('question', '')
    option1 = request.POST.get('option1', '')
    option2 = request.POST.get('option2', '')
    option3 = request.POST.get('option3', '')
    option4 = request.POST.get('option4', '')
    correct_answer = request.POST.get('correct_answer', '')
    solution = request.POST.get('solution', '')
    question_full=questions(question=question,option1=option1,option2=option2,option3=option3,option4=option4,correct_answer=correct_answer,solution=solution)
    question_full.save()
    return render(request,'admin.html',{'questions1':questions1})


