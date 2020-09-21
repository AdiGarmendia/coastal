import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from coastalapp.models import Vehicle
from coastalapp.models import Employee
from ..connection import Connection





@login_required
def vehicle_form(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        template = 'vehicles/vehicle_form.html'
        context = {
            'all_employees': employees
        }

        return render(request, template, context)

def vehicle_edit_form(request, vehicle_id):

    if request.method == 'GET':
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        employees = Employee.objects.all()

        template = 'vehicles/vehicle_form.html'
        context = {
            'vehicle': vehicle,
            'all_employees': employees
        }

        return render(request, template, context)

    