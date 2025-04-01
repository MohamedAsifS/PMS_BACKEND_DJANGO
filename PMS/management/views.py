from django.shortcuts import render
# from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework import permissions,authentication
from rest_framework.decorators import api_view
import pandas as pd
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Student,Department,CompanyTable,PlacementRecord,CompanyDepartmentYear
from .seriliazer import StudentSerializer,CompanyTableSerializer,PlacementSerilizer,CompanyDepartmentwithYearSerilizer,StudentList,CompanyList,DepartmentSerilizer

from .permission import PermissionForCoordinator,PermissionForStaff

# Create your views here.
class StudnetsCreateExcel(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    # parser_classes = [MultiPartParser, FormParser]
    permission_classes=[PermissionForStaff,permissions.IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    
    
    def post(self, request, *args, **kwargs):
        file=request.FILES.get('file')
        
  
        if file is None:
            return Response({"error": "No file uploaded."}, status=404)
        
        store=pd.read_excel(file)
        
        if len(store.index)==0:
            return Response({"error": "send with Index/tile in yours Excel."}, status=404)
       
        
        

        for _, row in store.iterrows():
            print(row)
            department=Department.objects.get_or_create(department_name=row[1])
            
            to={'student_name':row[0], 'student_department':department.id,'marks':row[2], 
                'date_of_birth':row[3].date(),'year':row[4]}
           

            series=StudentSerializer(data=to)
            
            if series.is_valid(raise_exception=True):
                series.save()
       
            
            
            
            
           

           
            
        return Response({"message": "File Uploaded"}, status=201)
    
# want to create a CBV for uploading the student data for manual
class StudentCreateManual(CreateAPIView):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
  
    
    def post(self,request,*args,**kwargs):
         print(request.data.get('student_department'))
         departement=Department.objects.get(department_name=request.data.get('student_department'))
         print(departement,departement.id)
        
         
        
         data={
         "student_name": request.data.get('student_name'),
         "marks": request.data.get('marks'),
         "student_department":departement.id ,
         "date_of_birth": request.data.get('date_of_birth'),
         "year": request.data.get('year')}
         series=StudentSerializer(data=data)


         if series.is_valid(raise_exception=True):
             series.save()
         return Response({"message":"File Uploaded"},status=201)

@api_view(['GET'])      
def list_student(request):
    department='MCA'
    print(request.GET.get('department'))
    students = Student.objects.select_related('student_department').filter(
        student_department__department_name=request.GET.get('department')
    )
    series=StudentList(students,many=True)
   
    return Response(series.data)
        
@api_view(['GET'])      
def list_department(request):
    get=Department.objects.all()
    data=DepartmentSerilizer(get,many=True)
    
    return Response(data.data)  
    
    
@api_view(['GET'])
def list_company(request):
    print(request.GET.get('department'))
    modle=CompanyDepartmentYear.objects.select_related('department').filter(department__department_name=request.GET.get('department'))
    series=CompanyList(modle,many=True)
    return Response(series.data)

class CompanyCreateExcel(CreateAPIView):
    queryset = CompanyTable.objects.all()
    serializer_class=CompanyTableSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[PermissionForStaff,permissions.IsAuthenticated]
    
    def post(self,request,*args,**kwargs):
        
        file=request.FILES.get('file')
        
        
        if file is None:
            return Response({"error": "No file uploaded."}, status=404)
        store=pd.read_excel(file)
        if len(store.index)==0:
            return Response({"error": "send with Index/tile in yours Excel."}, status=404)
        
        for _,row in store.iterrows():
            print('as')
            to={"company_name":row[0],'company_location':row[1]}
            print(to,"as")
            
            series=CompanyTableSerializer(data=to)
            if series.is_valid(raise_exception=True):
                series.save()
            
            
        return Response({"message":"File Uploaded"},status=201)

    
    
class PlacementRecordCreater(CreateAPIView):
    queryset = PlacementRecord.objects.all()
    serializer_class=PlacementSerilizer
    authentication_classes=[JWTAuthentication]
    permission_classes=[PermissionForCoordinator,permissions.IsAuthenticated]
    authentication_classes=[authentication.SessionAuthentication]
    def post(self,request,*args,**kwargs):
        print(request.POST)
        student=Student.objects.filter(student_name=request.POST.get('student')).first()
        company=CompanyTable.objects.get(company_name=request.POST.get('company'))
        department=Department.objects.get(department_name=request.POST.get('department'))
        if student is None or company is None:
            return Response({"error":"Student or Company not found"},status=404)
        series=PlacementSerilizer(data=request.data)
        if series.is_valid(raise_exception=True):
               series.save(student=student, company=company,department=department)
        return Response({"message":"Placement Record Created"},status=201)
    
    
class CompanyDepartmentYearCreate(CreateAPIView):
    queryset=CompanyDepartmentYear.objects.all()
    serializer_class=CompanyDepartmentwithYearSerilizer
    authentication_classes=[JWTAuthentication]
    permission_classes=[PermissionForStaff,permissions.IsAuthenticated]
   
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.data.get('company.company_name'),request.data.get('department'))
        company,_=CompanyTable.objects.get_or_create(company_name=request.data.get('company.company_name'),company_location=request.data.get('company.company_location')) #here we get tuple so we need to unpack
        department,_=Department.objects.get_or_create(department_name=request.data.get('department'))
        
        data = {
    "company": {"company_name":company.company_name,
               "company_location":company.company_location },  # Send ID instead of object
    "department": department.id,
    "year": request.data.get('year')
}
        series=CompanyDepartmentwithYearSerilizer(data=data)
        if series.is_valid(raise_exception=True):
            series.save(company=company,department=department)
        return Response({"message":"Department Year Created"},status=201)

class RetriveDataPlacementRecord(ListAPIView):
    serializer_class=PlacementSerilizer
    queryset=PlacementRecord.objects.all()
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        student_name=self.request.GET.get('student_name')
        print(student_name)
        company=self.request.GET.get('company')
        department=self.request.GET.get('department')
        status=self.request.GET.get('status')
        year=self.request.GET.get('year')
      
        return PlacementRecord.objects.get_params_record(student_name=student_name,company=company,department=department,status=status,year=year)
       
            
        
       
       
class RetriveCompany(ListAPIView):
    serializer_class=CompanyDepartmentwithYearSerilizer
    queryset=CompanyDepartmentYear.objects.all()
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        year=self.request.GET.get('year')
        department=self.request.GET.get('department')

        return CompanyDepartmentYear.objects.get_params_company(year=year,department=department)

    