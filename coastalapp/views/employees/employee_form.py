import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from coastalapp.models import Department
from coastalapp.models import Employee
from ..connection import Connection
# from ..employees.employee_details import get_employee
from ..departments.department_list import department_list


def employee_form(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        template = 'employees/employee_form.html'
        context = {
            'all_departments': departments
        }

        return render(request, template, context)

def employee_edit_form(request, employee_id):

    if request.method == 'GET':
        employee = Employee.objects.get(pk=employee_id)
        departments = Department.objects.all()

        template = 'employees/employee_form.html'
        context = {
            'employee': employee,
            'all_departments': departments
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        if request.method == (
            "actual_method" in form_data and form_data["actual_method"] == "PUT"
        ):
            form_data = request.PUT
            print("suncess")
            employee_edit = Employee.objects.get(pk=employee_id)
            employee_edit.first_name = form_data['first_name']
            employee_edit.last_name = form_data['last_name']
            employee_edit.start_date = form_data['start_date']
            employee_edit.is_supervisor = form_data['is_supervisor']
            employee_edit.department_id = form_data['department_id']
            # employee_edit.save()

        else: 
            print('failed')
            return redirect("coastalapp:employee_list")
        return redirect("coastalapp:employee_list")

        #     return redirect(reverse('coastalapp:employee', args=[employee_id]))
        # return redirect(reverse('coastalapp:employee', args=[employee_id]))
             

        