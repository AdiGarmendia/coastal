import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from coastalapp.models import Department
from coastalapp.models import Employee
from ..connection import Connection
from ..employees.employee_details import get_employee
from ..departments.department_details import get


def employee_form(request):
    if request.method == 'GET':
        departments = get_departments()
        template = 'employees/employee_form.html'
        context = {
            'all_departments': departments
        }

        return render(request, template, context)

def employee_edit_form(request, employee_id):

    if request.method == 'GET':
        employee = get_employee(employee_id)
        departments = get_departments()

        template = 'employees/employee_form.html'
        context = {
            'employee': employee,
            'all_departments': departments
        }

        return render(request, template, context)
             

        