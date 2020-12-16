from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from . url import *
from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,logout
from login.models import *
from django.template import RequestContext

# Create your views here.
def home(request):
    if request.method == 'POST':#post only
        Enrollment = request.POST.get('Enrollment')
        password = request.POST.get('password')
        response = render(request,'home.html')
        if Enrollment:#true enrollment
            user = auth.authenticate(enrollment= Enrollment, password=password)
        else:#non true
            return render(request, 'home_error.html')
        if user is not None:#true user
            Data = Account.objects.filter(enrollment=Enrollment)
            for e in Data:
                HOD = e.is_HOD
                Faculty = e.is_Faculty
                Enrollment = e.enrollment
                first = e.first_name
                last = e.last_name
            if HOD:
                login(request, user)
                response = render(request, 'HOD.html',{'Enrollment':Enrollment})
                response.set_cookie('enrollment',Enrollment)
                return response
            elif Faculty:
                login(request,user)
                for e in Data:
                    enrollment = e.enrollment
                response = render(request, 'Faculty.html',{'Enrollment':enrollment})
                response.set_cookie('enrollment',enrollment)
                return response
            else:
                login(request,user)
                stud = Student.objects.filter(Enrollment__enrollment__contains=Enrollment)
                for i in stud:
                    room = i.classname
                response = render(request, 'student.html',{'Enrollment':Enrollment})
                response.set_cookie('enrollment',Enrollment)
                response.set_cookie('classname',room)
                return response
        else:
            return render(request, 'home_error.html')
    else:
        return render(request, 'home.html')

def view(request):
    return render(request, 'register.html')

def register(request):
    enrollment = request.POST.get('Enrollment_number')
    email = request.POST.get('Email')
    password1 = request.POST.get('password')
    password2 = request.POST.get('confirm_password')
    first_name = request.POST.get('name')
    last_name = request.POST.get('LastName')
    new_account = Account(
        first_name=first_name,
        last_name=last_name,
        enrollment=enrollment,
        Email=email,
    )
    new_account.set_password(password1)
    new_account.save()
    return render(request, 'home.html')
def forgot(request):
    return render(request, 'forgot.html')

def lout(request):
    logout(request)
    respons = render(request, 'home.html')
    respons.delete_cookie('enrollment')
    return respons