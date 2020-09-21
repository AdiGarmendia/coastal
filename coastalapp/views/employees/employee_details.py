import sqlite3
from django.shortcuts import render, reverse, redirect
from coastalapp.models import Employee
from ..connection import Connection




def employee_details(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if request.method == "GET":
        template = "employees/employee_details.html"

        return render(request, template, {"employee": employee})

    elif request.method == 'POST':
        form_data = request.POST
        print(form_data["actual_method"])
        if (
            "actual_method" in form_data and form_data["actual_method"] == "PUT"
        ):
            form_data = request.POST
            print("suncess")
            employee.first_name = form_data['first_name']
            employee.last_name = form_data['last_name']
            employee.is_supervisor = form_data['is_supervisor']
            employee.department_id = form_data['department_id']
            employee.save()

        elif (
            "actual_method" in form_data and form_data["actual_method"] == "DELETE"
        ):
            employee.delete()
            return redirect(reverse('coastalapp:employee_list'))

            

        return redirect(reverse('coastalapp:employee', args=[employee_id]))