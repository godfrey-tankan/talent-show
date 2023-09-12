from django.urls import path ,include
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	# path('login/', views.login_user, name='login'),
	path('upload/', views.upload, name='upload'),
	path('logout/', views.logout_user, name='logout'),
	path('register/', views.register_user, name='register'),
	path('record/<int:pk>', views.company_record, name='record'),
	path('delete_company/<int:pk>', views.delete_company, name='delete_company'),
	path('add_record/', views.add_record, name='add_record'),
	path('update_company/<int:pk>', views.update_company, name='update_company'),



	path('employee_record/<int:pk>', views.employee_record, name='employee_record'),
	path('delete_employee/<int:pk>', views.delete_employee, name='delete_employee'),
	path('add_employee/', views.add_employee, name='add_employee'),
	path('update_employee/<int:pk>', views.update_employee, name='update_employee'),



	path('department_record/<int:pk>', views.department_record, name='department_record'),
	path('delete_department/<int:pk>', views.delete_department, name='delete_department'),
	path('add_department/', views.add_department, name='add_department'),
	path('update_department/<int:pk>', views.update_department, name='update_department'),


	path('company_details/', views.company_details, name='company_details'),



]