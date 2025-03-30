from django.db import models
import datetime
from .CustomQuerySet import PlacementManger

from user.models import User

date=datetime.datetime.now().year

class Department(models.Model):
  
   department_name=models.CharField(max_length=8,unique=True,null=True)
   
   def __str__(self) -> str:
          if self.department_name==None:
              print(self.department_name)
              return "Department not available"
          else:
              return self.department_name
        
            
     
# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=30)
    student_department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)  
    marks = models.DecimalField(max_digits=30, decimal_places=2)
    date_of_birth = models.DateField()
    year = models.IntegerField(default=datetime.date.today().year)  
    
    def __str__(self) -> str:
        return self.student_name

    
class CompanyTable(models.Model):
    company_name = models.CharField(max_length=50,null=True)
    company_location = models.CharField(max_length=50,null=True)
    
    # def __str__(self) -> str:
    #     return self.company_name
    
class PlacementRecord(models.Model):
    STATUS_CHOICES = [
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
        ('shortlisted', 'Shortlisted'),
        ('waiting_list', 'Waiting List'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  
    company = models.ForeignKey(CompanyTable, on_delete=models.SET_NULL, null=True) 
    department=models.ForeignKey(Department, on_delete=models.SET_NULL,default=None,null=True)
    role = models.CharField(max_length=30)
    year = models.IntegerField(default=datetime.date.today().year)  
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='waiting_list')  
    
    objects=PlacementManger()
class CompanyDepartmentYear(models.Model):
    company = models.ForeignKey(CompanyTable, on_delete=models.CASCADE)  
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.IntegerField(default=datetime.date.today().year)
    
    objects=PlacementManger()

    class Meta:
        unique_together = ("company", "department", "year")  

    