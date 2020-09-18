import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from coastalapp.models import Employee
from ..connection import Connection



def employee_list(request):
    if request.method == 'GET':
        all_employees = Employee.objects.all()
        template = 'employees/employees_list.html'
        context = {
            'employees': all_employees
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_employee = Employee()
        new_employee.first_name = form_data['first_name']
        new_employee.last_name = form_data['last_name']
        new_employee.start_date = form_data['start_date']
        new_employee.is_supervisor = form_data['is_supervisor']
        new_employee.department_id = form_data['department_id']
        new_employee.save()

        return redirect(reverse('coastalapp:employee_list'))