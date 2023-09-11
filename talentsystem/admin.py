from django.contrib import admin
from .models import CompanyRecord, EmployeeRecord, DepartmentRecord

# Register your models here.
admin.site.register(CompanyRecord)
admin.site.register(EmployeeRecord)
admin.site.register(DepartmentRecord)
