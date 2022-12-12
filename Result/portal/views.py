from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from django.contrib import messages
from django.contrib import admin
from django.contrib.auth import authenticate
from .forms import StudentForm
# Create your views here.
def index(request):
    return render(request,"home.html")
def marks(request):
    Reg=request.GET['Reg']
    BirthDate=request.GET['BirthDate']
    student=Student.objects.filter(Reg=Reg,BirthDate=BirthDate)
    if len(student)==0:
        messages.error(request,'Register no or date of birth not correct')
        return redirect('index')
    return render(request,'StuMarks.html',{'student':student[0]})
def adminlog(request):
    return render(request,'login.html')
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            return redirect('action')
        else:
            messages.error(request,'username or password is wrong')
            return redirect('login')
    
def action(request):
    form=StudentForm()
    students=Student.objects.all().values()
    return render(request,'alert.html',{'form':form,'students':students})
def add(request):
    try:
        Reg=request.GET['Reg']
        BirthDate=request.GET['BirthDate']
        Math=request.GET['Math']
        Science=request.GET['Science']
        Social=request.GET['Social']
        t=Student(Reg=Reg,BirthDate=BirthDate,Math=Math,Science=Science,Social=Social)
        t.save()
        messages.sucess(request, "Your data added Sucessfully")
    except:
         messages.error(request, "Your have error in adding data")
    return redirect('action')
def delete(request,Reg):
    s=Student.objects.get(Reg=Reg)
    s.delete()
    return redirect('action')