from django.urls import path
from .views import StudnetsCreateExcel,CompanyCreateExcel,PlacementRecordCreater,CompanyDepartmentYearCreate,RetriveDataPlacementRecord,RetriveCompany,StudentCreateManual,list_student,list_company,list_department

urlpatterns = [
    path('excelstudents',StudnetsCreateExcel.as_view()),
    path('excelcompany',CompanyCreateExcel.as_view()),
    path('manualstudents',StudentCreateManual.as_view()),
    path('staterecords',PlacementRecordCreater.as_view()),
    path('companyyear',CompanyDepartmentYearCreate.as_view()),
    path('retriverecord',RetriveDataPlacementRecord.as_view()),
    path('retrivecompany',RetriveCompany.as_view()),
    path('liststudent',list_student),
    path('listcompany',list_company),
    path('listdepartment',list_department)
]
