from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    name=models.CharField(max_length=50)
    departement=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=75)
    zipcode=models.CharField(max_length=75)
    state=models.CharField(max_length=75)
    active=models.BooleanField(default=True)
    on_leave=models.BooleanField(default=False)
    email=models.EmailField()
    leave_count=models.IntegerField(default=0,null=True,blank=True)
    address=models.CharField(max_length=75,null=True,blank=True)
    dob=models.DateField(blank=True,null=True)

    def __str__(self):
        return self.name