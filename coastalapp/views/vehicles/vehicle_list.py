import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from ..connection import Connection
from coastalapp.models import Vehicle


def vehicle_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                v.id,
                v.make,
                v.purchase_date,
                v.retired_date,
                v.manufacturer
            from coastalapp_vehicle v
            """)

            all_vehicles = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                vehicle = Vehicle()
                vehicle.id = row['id']
                vehicle.make = row['make']
                vehicle.purchase_date = row['purchase_date']
                vehicle.retired_date = row['retired_date']
                vehicle.manufacturer = row['manufacturer']

                all_vehicles.append(vehicle)

        template = 'vehicles/vehicle_list.html'
        context = {
            'vehicles': all_vehicles
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                INSERT INTO coastalapp_vehicle
                (
                    manufacturer, make, purchase_date, retired_date
                    )
                VALUES (?, ?, ?, ?)
                """,
                              (form_data['manufacturer'], form_data['make'], form_data['purchase_date'], form_data['decommission_date']))

            return redirect(reverse('coastalapp:vehicle_list'))