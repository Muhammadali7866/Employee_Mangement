from email import message
from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import Signupform,EmployeeForm,LoginForm
from .models import Employee
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.
def index(request):
    data=Employee.objects.all()
    on_leve=data.filter(on_leave=True)
    return render(request,'main/index.html',{"total_employee":data.count(),"on_leave":on_leve.count()})

def user_signup(request):
    if request.method=="POST":
        fm=Signupform(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/login/")
    else:
        fm=Signupform()
    return render(request,"main/signup.html",{"form":fm})

def user_login(request):
    if not  request.user.is_authenticated:
        if request.method=="POST":
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data["username"]
                upass=fm.cleaned_data["password"]
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return redirect("/")
        else:
            fm=LoginForm()
        return render(request,"main/login.html",{"form":fm})
    else:
        return redirect("/")

        

def add_emploee(request):
    if request.method=="POST":
        fm=EmployeeForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/")
    else:
        fm=EmployeeForm()
    return render(request,'main/add.html',{"form":fm})

def edit_employee(request,id):
    if request.method=="POST":
        user=Employee.objects.get(id=id)
        fm=EmployeeForm(request.POST,instance=user)
        if fm.is_valid():
            fm.save()
            return redirect("/view/")
    else:
        user=Employee.objects.get(id=id)
        fm=EmployeeForm(instance=user)

    return render(request,'main/edit.html',{"form":fm},)


def view_employee(request):
    fm=Employee.objects.all()
    return render(request,"main/view.html",{"form":fm})

def delete_employee(request,id):
    user=Employee.objects.get(id=id)
    user.delete()
    return redirect("/view/")
def leave_status(request,pid):
    data=Employee.objects.get(id=pid)
    if data.on_leave:
        data.on_leave=False
    else:
        data.leave_count=data.leave_count+1
        data.on_leave=True
    data.save()
    messages.success(request,"Employeee leave status is changed :")
    return redirect("/view/")
