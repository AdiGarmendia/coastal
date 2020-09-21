import sqlite3
from django.shortcuts import render, reverse, redirect
from coastalapp.models import Department
from ..connection import Connection




def department_details(request, department_id):
    if request.method == "GET":
        department = Department.objects.get(pk=department_id)
        template = "departments/department_details.html"

        return render(request, template, {"department": department})