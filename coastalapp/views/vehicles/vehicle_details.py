import sqlite3
from django.shortcuts import render, reverse, redirect
from coastalapp.models import Vehicle
from coastalapp.models import Employee
from ..connection import Connection


def get_vehicle(vehicle_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row

        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
                v.id,
                v.make,
                v.purchase_date,
                v.retired_date,
                v.manufacturer
            from coastalapp_vehicle v
        WHERE v.id = ?
        """, (vehicle_id,))

        return db_cursor.fetchone()


def vehicle_details(request, vehicle_id):
    if request.method == "GET":
        vehicle = get_vehicle(vehicle_id)
        template = "vehicles/vehicle_details.html"

        return render(request, template, {"vehicle": vehicle})

    if request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for deleting a book
        #
        # Note: You can use parenthesis to break up complex
        #       `if` statements for higher readability
    if (
        "actual_method" in form_data
        and form_data["actual_method"] == "DELETE"
    ):
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            DELETE FROM coastalapp_vehicle
            WHERE id = ?
            """, (vehicle_id,))
        return redirect(reverse('coastalapp:vehicle_list'))