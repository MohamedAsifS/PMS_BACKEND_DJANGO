from django.contrib import admin
from .models import CompanyDepartmentYear,Student,Department,CompanyTable,PlacementRecord

# Register your models here.
admin.site.register(CompanyDepartmentYear)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(CompanyTable)
admin.site.register(PlacementRecord)