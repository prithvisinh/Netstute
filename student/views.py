from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import logout
from login.models import *
from .forms import uploadform
from .models import stupload,links

# Create your views here.
def home(request):
    enroll=request.COOKIES.get("enrollment")
    stud = Student.objects.filter(Enrollment__enrollment__contains=enroll)
    for i in stud:
        field = i.field
        room = i.classname
    lecture = SubjectUpload.objects.filter(classname= room)
    response = render(request, 'student/home.html',{'lec':lecture,'field':field})
    response.set_cookie('classname',room)
    response.set_cookie('field',field)
    return response

def edit(request):
    return render(request, 'student/edit.html')


def attendance(request):
    return render(request, 'student/attendance.html')


def chat(request):
    return render(request, 'student/chat.html')


def practical(request):
    practical = uploadform(request.POST)
    data = request.COOKIES.get("classname")
    uploads = stupload.objects.filter(classname = data)
    return render(request, 'student/practical.html',{"prac":practical,'upload':uploads})


def request(request):
    return render(request, 'student/request.html')


def student_subject(request):
    subject = request.COOKIES.get("classname")
    sub = Classroom.objects.all().filter(classname=subject)
    return render(request, 'student/student_subject.html',{'subject':sub})


def subject_class(request):
    Classname = request.COOKIES.get("classname")
    link = links.objects.filter(classname = Classname)
    return render(request, 'student/subject_class.html',{'links':link})

def view_logout(request):
    logout(request)
    return render(request, 'home.html')