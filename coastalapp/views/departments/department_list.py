import sqlite3
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from coastalapp.models import Department, Employee
from ..connection import Connection





def department_list(request):
    if request.method == 'GET':

        all_departments = Department.objects.all()
        template = 'departments/department_list.html'
        context = {
            'departments': all_departments
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

    

        new_department = Department()
        new_department.department_name = form_data['department_name']
        new_department.save()

        return redirect(reverse('coastalapp:department_list'))