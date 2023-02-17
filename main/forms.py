from tkinter import Widget
from turtle import width
from xml.dom.minidom import Attr
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Employee
from django.contrib.auth import authenticate

class Signupform(UserCreationForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        widgets = {
                    'username': forms.TextInput(
                        attrs={
                            'class': 'form-control'
                        }
                    ),
                    "email":forms.EmailInput(attrs={"class":"form-control"})
                }

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=["name","email","city","country","departement","address","zipcode","state","dob"]
        widgets={
           "name": forms.TextInput(attrs={"class":"form-control"}),
           "email":forms.EmailInput(attrs={"class":"form-control"}),
           "country": forms.TextInput(attrs={"class":"form-control"}),
            "departement":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "state":forms.TextInput(attrs={"class":"form-control"}),
           "zipcode": forms.TextInput(attrs={"class":"form-control"}),
           "dob": forms.DateInput(attrs={"class":"form-control"}),
          # "on_leave": forms.CheckboxInput(attrs={"class":"form-control"}),
         # "leave_count": forms.TextInput(attrs={"class":"form-control"}),
            "city": forms.TextInput(attrs={"class":"form-control"}),


        }
        labels={"dob":"Date Of Birth"}