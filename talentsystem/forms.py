
import os
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import CompanyRecord, EmployeeRecord, DepartmentRecord
from django.core.exceptions import ValidationError
import csv

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	




class AddCompanyRecord(forms.ModelForm):

	company_name = forms.CharField(required=True, widget =forms.widgets.TextInput(attrs={"placeholder":"Company Name", "class":"form-control"}),label="")
	company_reg_number = forms.CharField(required=True, widget =forms.widgets.TextInput(attrs={"placeholder":"Company Registration Number", "class":"form-control"}),label="")
	company_address = forms.CharField(required=True, widget =forms.widgets.TextInput(attrs={"placeholder":"Company Address", "class":"form-control"}),label="")
	contact_person = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Contact Person ", "class":"form-control"}),label="")
	departments = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Departments", "class":"form-control"}),label="")
	contact_phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Company ContactPhone", "class":"form-control"}),label="")
	number_of_employees = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Number of Employees", "class":"form-control"}),label="")
	company_email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Email Address", "class":"form-control"}),label="")
	class Meta:
		model = CompanyRecord
		exclude = ("User",)


class AddEmployeeRecord(forms.ModelForm):

	employee_name = forms.CharField(required=True, widget =forms.widgets.TextInput(attrs={"placeholder":"| EMployee Name", "class":"form-control"}),label="")
	employee_id = forms.CharField(required=True, widget =forms.widgets.TextInput(attrs={"placeholder":"| Employee ID Number", "class":"form-control"}),label="")
	role = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"| Employee Role ", "class":"form-control"}),label="")
	date_started = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"| Date Started In Role(dd-mm-yyy)", "class":"form-control"}),label="")
	date_left = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"| Date Left Role (dd-mm-yyy)", "class":"form-control"}),label="")
	dutie = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"| Duty Served (Serving)", "class":"form-control"}),label="")
	class Meta:
		model = EmployeeRecord
		exclude = ("User",)

class AddDepartment(forms.ModelForm):
	department_name = forms.CharField(required=True, widget =forms.widgets.TextInput(attrs={"placeholder":"| Department Name", "class":"form-control"}),label="")
	
	class Meta:
		model = DepartmentRecord
		exclude = ("User",)



class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select a file')

    def clean_file(self):
        uploaded_file = self.cleaned_data['file']
        if not uploaded_file.name.endswith('.csv'):
            raise forms.ValidationError("Only CSV files are allowed.")
        try:
            csv.reader(uploaded_file)
        except csv.Error:
            raise forms.ValidationError("Invalid CSV file.")
        return uploaded_file