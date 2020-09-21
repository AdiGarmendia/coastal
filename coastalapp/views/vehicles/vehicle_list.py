import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from ..connection import Connection
from coastalapp.models import Vehicle


def vehicle_list(request):
    if request.method == 'GET':
        all_vehicles = Vehicle.objects.all()
        template = 'vehicles/vehicle_list.html'
        context = {
            'vehicles': all_vehicles
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_vehicle = Vehicle()
        new_vehicle.make = form_data['make']
        new_vehicle.manufacturer = form_data['manufacturer']
        new_vehicle.purchase_date = form_data['purchase_date']
        new_vehicle.retired_date = form_data['retired_date']
        new_vehicle.save()

        return redirect(reverse('coastalapp:vehicle_list'))