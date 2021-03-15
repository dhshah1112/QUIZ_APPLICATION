from django.urls import path,include
from django.conf.urls import url

from quizdb import views

urlpatterns = [
   # path('', views.index, name='index'),
    url('addstudentinfo/', views.addstudentinfo),
    url(r'^delstudentinfo/$', views.delstudentinfo),
    
   
    url(r'^delunsuccess/$', views.delunsuccess),
    url(r'^getusername_del/$', views.getusername_del),
    url(r'^viewinfo/$', views.viewinfo),
    url(r'^updateinfo/$', views.updateinfo),
    url(r'^getusername_update/$', views.getusername_update),
    url(r'^addquestioninfo/$', views.addquestioninfo),
    #url(r'^addquestion/$', views.addquestion),
    url('addteacher_questioninfo/', views.addteacher_questioninfo),
    #url(r'^addteacher_question/$', views.addteacher_question),
    url('add_quiz/', views.add_quiz),
    url('give_quiz/', views.give_quiz),
    url('validate_answer/', views.validate_answer),
    #url(r'^create_quiz/$', views.create_quiz),
    path('students/', views.StudentListView.as_view(), name = 'students'),
]