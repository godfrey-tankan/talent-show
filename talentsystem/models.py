from django.db import models


# Company datails
class CompanyRecord(models.Model):
	company_name = models.CharField(max_length=100)
	company_reg_number = models.CharField(max_length=50)
	company_address = models.CharField(max_length=150)
	company_email = models.EmailField(max_length=100)
	contact_person = models.CharField(max_length=50)
	departments = models.CharField(max_length=300)
	contact_phone = models.CharField(max_length=50)
	number_of_employees = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add =True)
	bulk = models.FileField(null = True, blank=True)

	def __str__ (self):
		return(f"{self.company_name}{self.company_reg_number}")



# Department Details
class DepartmentRecord(models.Model):
    department_name = models.CharField(max_length=100)
    # company = models.ForeignKey(CompanyRecord, on_delete=models.CASCADE)

    def __str__ (self):
    	return(f"{self.id }{self.department_name}")


# Employee Details
class EmployeeRecord(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50)
    # department = models.ForeignKey(DepartmentRecord, on_delete=models.CASCADE)
    role = models.CharField(max_length=150)
    date_started = models.CharField(max_length=50)
    date_left = models.CharField(max_length=50)
    dutie = models.CharField(max_length=300)
    def __str__ (self):
    	return(f"{self.employee_name}{self.employee_id}")



