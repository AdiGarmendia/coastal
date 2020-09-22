import sqlite3
from django.shortcuts import render, reverse, redirect
from coastalapp.models import Vehicle
from ..connection import Connection





def vehicle_details(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    if request.method == "GET":
        template = "vehicles/vehicle_details.html"

        return render(request, template, {"vehicle": vehicle})

    elif request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data and form_data["actual_method"] == "PUT"
        ):
            print('form_data', form_data)
            
            vehicle.employee_id = form_data['employee_id']
            vehicle.save()

        elif (
            "actual_method" in form_data and form_data["actual_method"] == "DELETE"
        ):
            vehicle.delete()
            return redirect(reverse('coastalapp:vehicle_list'))

            

        return redirect(reverse('coastalapp:vehicle', args=[vehicle_id]))