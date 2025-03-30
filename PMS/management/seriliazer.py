from rest_framework import serializers

from .models import Student,CompanyTable,PlacementRecord,CompanyDepartmentYear,Department

class StudentSerializer(serializers.ModelSerializer):
    # student_department = serializers.CharField(source="department.department_name",write_only=True) 
   
    class Meta:
        model=Student
        fields=['student_name','marks','student_department','date_of_birth','year']
    
        
class StudentList(serializers.ModelSerializer):
    student_department = serializers.CharField(source="student_department.department_name")
    class Meta:
        model=Student
        fields=['student_name','student_department']
    
        
class CompanyList(serializers.ModelSerializer):
    department=serializers.CharField(source='department.department_name')
    company=serializers.CharField(source='company.company_name')
    class Meta:
        model=CompanyDepartmentYear
        fields=['company','department','year']
   
        
class CompanyTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyTable
        fields=['company_name','company_location']
        
        
class PlacementSerilizer(serializers.ModelSerializer):
    class Meta:
        Student=serializers.CharField(source="Student.student_name")
        model=PlacementRecord
        fields=['student','company','department','role','year','status']
        
class CompanyDepartmentwithYearSerilizer(serializers.ModelSerializer):
    company=CompanyTableSerializer()
    department = serializers.CharField(source="department.department_name") 
    depth=1
    class Meta:
        model=CompanyDepartmentYear
        fields=['company','department','year']
class DepartmentSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=['department_name']