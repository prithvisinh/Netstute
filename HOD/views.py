from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout as lout
from login.views import home
import os
from django.core.files import File
from login.forms import *
from .models import *
from login.models import *
# Create your views here.
def home(request):
    lecture = SubjectUpload.objects.all()
    return render(request,'HOD/home.html',{'lecture':lecture})


def edit(request):
    return render(request, 'HOD/edit.html')


def clas(request):
    timetable = timetableHOD.objects.all()
    return render(request, 'HOD/class.html', {'timetable':timetable})


def add(request):
    create = registerform(request.POST)
    return render(request, 'HOD/add.html',{"create":create})


def deatin(request):
    return render(request, 'HOD/detain.html')


def promotion(request):
    faculty = Faculty.objects.all()
    students = Student.objects.all()
    return render(request, 'HOD/promotion.html',{'faculty':faculty,'student':students})


def attendance(request):
    return render(request, 'HOD/attendance.html')


def faculty_subject(request):
    return render(request, 'HOD/faculty_subject.html')


def prac_class(request):
    return render(request, 'HOD/prac_class.html')


def practical_submit(request):
    return render(request, 'HOD/practical_submit.html')


def request(request):
    return render(request, 'HOD/request.html')


def subject_upload(request):
    return render(request, 'HOD/subject_upload.html')


def add_faculty(request):
    return render(request, 'HOD/add_faculty.html')


def add_student(request):
    return render(request, 'HOD/add_student.html')


def allocate(request):
    return render(request, 'HOD/allocate.html')

def remove_faculty(request):
    return render(request, 'HOD/remove_faculty.html')


def remove_student(request):
    return render(request, 'HOD/remove_student.html')


def logout(request):
    lout(request)
    return render(request, 'home.html')