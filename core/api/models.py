from django.db import models

# Create your models here.,
# creating company model

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices = (
        ('IT','IT'),
        ('Non IT','NON IT'),
        ('BB','BB'))
    )
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default = True)

# creating employee models
class Employee(models.Model):
    Employee_Name = models.CharField(max_length=50)
    Employee_Email = models.CharField(max_length=20)
    Employee_Address = models.CharField(max_length=200)
    Employee_phone = models.CharField(max_length=20)
    Employee_Position = models.CharField(max_length=50,choices = (
        ('Manager','Manager'),
        ('Software Dev','Developer'),
        ('HR','HR')
    ))
    #here we creating relation between company to employee
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
