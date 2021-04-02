from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from reportlab.pdfgen import canvas
#import pymysql
from quizdb.models import user1
from django.views import generic
from django.template.context_processors import csrf
from quizdb.models import questions
from quizdb.models import quiz
from quizdb.models import teacher_questions
import emoji
import unicodedata
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
    student = User.objects.filter(username = user_name)
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
    student = User.objects.filter(username = user_name)
    if not student :
        return HttpResponseRedirect('/quizdb/delunsuccess/')
    else:
        for s in student:
            s.delete()
        return  render(request,'delrecord.html')
def addquestioninfo(request):
     if request.method=='POST':
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
        return render(request,'add_quiz.html')
def give_quiz(request):
    questions1=questions.objects.all()
    return render(request,'give_quiz.html',{'questions1':questions1})

def validate_answer(request):
    cnt=0
    cnt2=0
    selectedOptions=[]
    correctAnswers=[]
    question_id=[]
    solution=[]
    ques=[]
    if request.method=="POST":
        questions1=questions.objects.all()
        for question in questions1:
            ques.append(question.question)
            selectedOptions.append(request.POST.get('question' + str(question.question_id),''))
            correctAnswers.append(question.correct_answer)
            question_id.append(question.question_id)
            cnt2=cnt2+1
            solution.append(question.solution)
    i=0
    j=0
    l=len(selectedOptions)
    while(l):
            if selectedOptions[i]==correctAnswers[j]:
                cnt=cnt+1
            i=i+1
            j=j+1 
            l=l-1    
    mylist=zip(selectedOptions,correctAnswers,question_id,solution,ques)
    accuracy=(cnt/cnt2)*100
    return render(request,'validate_answer.html',{'mylist':mylist,'cnt':cnt,'cnt2':cnt2,'accuracy':accuracy, 'questions1':questions1})    
        
def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="Result.pdf"' 
    message="You need more practice"
    accuracy=request.POST.get('Accuracy')
   
    total_question=request.POST.get('Total_Questions')
    correct_answers=request.POST.get('Correct_Answers')
   
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 30) 
    p.setFillColorRGB(1,0,0)
     
    if float(accuracy)>= 50:
        p.setFillColorRGB(0,0,0)
        message="Well Done"
    p.drawString(200,800, "Result")
    p.drawString(100,600,"Total questions" + " = " +str(total_question))
    p.drawString(100,500,"Correct answers" + " = " +str(correct_answers)) 
    p.drawString(100,400,"Accuracy" + " = " +str(accuracy)+"%") 
    p.drawString(100,300,message)
    
           
    p.showPage()  
    p.save()  
    return response  