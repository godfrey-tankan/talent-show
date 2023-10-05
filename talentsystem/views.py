

from django.shortcuts import render ,redirect, HttpResponse
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from .forms import SignUpForm, AddCompanyRecord, AddEmployeeRecord, AddDepartment , UploadFileForm
from .models import CompanyRecord, DepartmentRecord, EmployeeRecord
from cryptography.fernet import Fernet










# Create your views here.
def home(request):
	company_Records = CompanyRecord.objects.all()
	department_Records = DepartmentRecord.objects.all()
	employee_Records = EmployeeRecord.objects.all()



	# checking and logging in usrr
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
	    context = {
	        'company_Records': company_Records,
	        'department_Records': department_Records,
	        'employee_Records': employee_Records
	    }
	    return render(request, 'home.html', context)


def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

def register_user(request):

	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()

			# Authenticate and login

			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
		else:
			form = SignUpForm()
			return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {})


# viewign individualcompany record
def company_record(request, pk):
	if request.user.is_authenticated:
		company_record = CompanyRecord.objects.get(id=pk)
		return render(request, 'record.html', {'company_record':company_record})

	else:
		messages.success(request, "Login to View the record!.")
		return redirect('home')




def delete_company(request,pk):
	if request.user.is_authenticated:
		delete_company = CompanyRecord.objects.get(id=pk)
		delete_company.delete()
		messages.success(request, "Company deleted.")
		return redirect('home')
	else:
		messages.success(request, "You don't have the right to delete this record.")
		return redirect('home')



def add_record(request):
	form = AddCompanyRecord(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record= form.save()
				messages.success(request, "Company Record Added!")
				return redirect('home')

		return render(request , 'add_record.html',{'form':form})
	else:
		messages.success(request, "Log In To Add Record.")
		return redirect('home')

def update_company(request, pk):
	if request.user.is_authenticated:
		current_company = CompanyRecord.objects.get(id=pk)
		form = AddCompanyRecord(request.POST or None, instance = current_company)
		if form.is_valid():
			form.save()
			messages.success(request, "Company Updated.")
			return redirect('home')
		return render(request, 'update_company.html', {'form':form})
	else:
		messages.success(request, "You must be looged in.")
		return redirect('home')






# Employee Records >>>>

def employee_record(request, pk):
	if request.user.is_authenticated:
		employee_record = EmployeeRecord.objects.get(id=pk)
		return render(request, 'employee_record.html', {'employee_record':employee_record})

	else:
		messages.success(request, "Login to View the record!.")
		return redirect('home')


# adding a new employee

def add_employee(request):
	form = AddEmployeeRecord(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record= form.save()
				messages.success(request, "Employee  Added!")
				return redirect('home')

		return render(request , 'add_employee.html',{'form':form})
	else:
		messages.success(request, "Log In To Add Record.")
		return redirect('home')

def update_employee(request, pk):
	if request.user.is_authenticated:
		current_employee= EmployeeRecord.objects.get(id=pk)
		form = AddEmployeeRecord(request.POST or None, instance = current_employee)
		if form.is_valid():
			form.save()
			messages.success(request, "Employee Updated.")
			return redirect('home')
		return render(request, 'update_employee.html', {'form':form})
	else:
		messages.success(request, "looged in to modify.")
		return redirect('home')

def delete_employee(request,pk):
	if request.user.is_authenticated:
		delete_it = EmployeeRecord.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Employee deleted.")
		return redirect('home')
	else:
		messages.success(request, "You don't have the right to delete this record.")
		return redirect('home')


# <<<<<End-Of-Employees-Records>>>>>>







# Start-of-Department-Records>>>

def department_record(request, pk):
	if request.user.is_authenticated:
		department_record = DepartmentRecord.objects.get(id=pk)
		return render(request, 'department_record.html', {'department_record':department_record})

	else:
		messages.success(request, "Login to View the record!.")
		return redirect('home')

# Adding a department

def add_department(request):
	form = AddDepartment(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record= form.save()
				messages.success(request, "New Department Added.")
				return redirect('home')

		return render(request , 'add_department.html',{'form':form})
	else:
		messages.success(request, "Log In To Add Record.")
		return redirect('home')

# Editing and updating the Departments Records>>>

def update_department(request, pk):
	if request.user.is_authenticated:
		current_department = DepartmentRecord.objects.get(id=pk)
		form = AddDepartment(request.POST or None, instance = current_department)
		if form.is_valid():
			form.save()
			messages.success(request, "Department Updated.")
			return redirect('home')
		return render(request, 'update_department.html', {'form':form})
	else:
		messages.success(request, "looged in to modify.")
		return redirect('home')


# Deleting Department record>>>>
def delete_department(request,pk):
	if request.user.is_authenticated:
		delete_it = DepartmentRecord.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Department deleted.")
		return redirect('home')
	else:
		messages.success(request, "You don't have the right to delete this record.")
		return redirect('home')



# Bulk Uploading Records


from django.shortcuts import render, redirect

def upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                file = form.cleaned_data['file']
                record = CompanyRecord.objects.create(bulk=file)
                record.save()
                return HttpResponse("Company record uploaded via bulk upload with id " + str(record.pk) + " file: " + str(record.bulk))
        else:
            form = UploadFileForm()
            return render(request, 'upload.html', {'form': form})
    else:
        return redirect('home')  # Redirect to the home page if the user is not authenticated


# All the Necessary Company Details
def company_details(request):
    companies = CompanyRecord.objects.all()
    return render(request, 'company_details.html', {'companies': companies})

def search_results(request):
    search_query = request.GET.get('search_query')
    results = EmployeeRecord.objects.filter(
        employee_name__icontains=search_query
    )
    context = {
        'results': results,
        'search_query': search_query,
    }
    return render(request, 'search_results.html', context)