from django.shortcuts import render
from django.contrib.auth import logout
from login.models import *
from HOD.models import *
from login.forms import *
from student.models import stupload
from student.forms import linkform

# Create your views here.
def home(request):
    classname = Classroom.objects.all()
    for i in classname:
        cname = i.classname
    upload = SubjectUpload.objects.filter(classname__classname__contains=cname)
    response = render(request,'Faculty/home.html',{'classname':classname,'upload':upload})
    return response

def edit(request):
    return render(request, 'Faculty/edit.html')


def clas(request):
    enrollment = request.COOKIES.get('enrollment')
    faculty = timetableHOD.objects.filter(Enrollment__enrollment__contains=enrollment)
    timetable = timetableStudent.objects.all()
    return render(request, 'Faculty/class.html',{'fac':faculty,'stu':timetable})


def add(request):
    form = registerform()
    return render(request, 'Faculty/add.html',{'form':form})


def detain(request):
    return render(request, 'Faculty/detain.html')


def promote(request):
    return render(request, 'Faculty/promotion.html')


def attendance(request):
    return render(request, 'Faculty/attendance.html')


def faculty_subject(request):
    return render(request, 'Faculty/faculty_subject.html')


def prac_class(request):
    link = linkform()
    return render(request, 'Faculty/prac_class.html',{'link':link})


def practical_submit(request):
    data = request.COOKIES.get("classname")
    uploads = stupload.objects.filter(classname = data)
    return render(request, 'Faculty/practical_submit.html',{'upload':uploads})


def request(request):
    return render(request, 'Faculty/request.html')


def subject_upload(request):
    upload = Subjectup()
    return render(request, 'Faculty/subject_upload.html',{'upload':upload})

def view_logout(request):
    logout(request)
    return render(request, 'home.html')