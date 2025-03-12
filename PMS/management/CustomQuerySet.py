
from django.db import models

class PlacementQuerySEt(models.QuerySet):
    def get_student(self,studentname):
        return self.filter(student__student_name__icontains=studentname)
    def get_company(self,companyname):
        print("In company")
        return self.filter(company__company_name__icontains=companyname)
    def get_department(self,departmenyname):
        return self.filter(department__department_name__icontains=departmenyname)
    def get_status(self,status):
        print("yes")
        return self.filter(status=status)
class RetriveDepartment(models.QuerySet):
    
    def get_Year(self,year):
        return self.filter(year=year)
    def get_department(self,department):
        print(department)
        return self.filter(department__department_name__icontains=department)
class PlacementManger(models.Manager):
    def get_queryset_record(self):
        
        return PlacementQuerySEt(self.model,using=self._db).all()
    
    def get_queryset_company(self):
        return RetriveDepartment(self.model,using=self._db).all()
        
    def get_params_record(self,**kwargs):
        student_name=kwargs.get('student_name')
        company_name=kwargs.get('company_name')
        department=kwargs.get('department')
        status=kwargs.get('status')
        
        # student_name,company_name,department,status
        querySet=self.get_queryset_record()
        if student_name:
            querySet=querySet.get_student(student_name)
        if company_name:
            querySet=querySet.get_company(company_name)
        if department:
            querySet=querySet.get_department(department)
        if status:
            querySet=querySet.get_status(status)
        print(status,student_name)
        
        return querySet
    def get_params_company(self,**kwargs):
        year=kwargs.get('year')
        department=kwargs.get('department')
        query=self.get_queryset_company()
        if year:
            query=query.get_Year(year)
        if department:
            query=query.get_department(department)
        return query