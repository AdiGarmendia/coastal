import sqlite3
from django.shortcuts import render
from ..connection import Connection
from coastalapp.models import Department

def department_form(request):
    if request.method == 'GET':

        template = 'departments/department_form.html'

        return render(request, template)