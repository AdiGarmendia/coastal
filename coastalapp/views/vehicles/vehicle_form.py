import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from coastalapp.models import Vehicle
from ..connection import Connection


def get_vehicles():
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

        return db_cursor.fetchall()


@login_required
def vehicle_form(request):
    if request.method == 'GET':
        vehicles = get_vehicles()
        template = 'vehicles/vehicle_form.html'
        context = {
            'all_vehicles': vehicles
        }

        return render(request, template, context)