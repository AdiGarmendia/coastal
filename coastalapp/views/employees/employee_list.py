import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from coastalapp.models import Employee
from ..connection import Connection


def employee_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                e.id,
                e.first_name,
                e.last_name,
                e.start_date,
                e.is_supervisor,
                e.department_id,
                d.id as department_id,
                d.department_name
            from coastalapp_employee e
            join coastalapp_department d on e.department_id = d.id
            """)

            all_employees = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                employee = Employee()
                employee.id = row['id']
                employee.first_name = row['first_name']
                employee.last_name = row['last_name']
                employee.start_date = row['start_date']
                employee.is_supervisor = row['is_supervisor']
                employee.department_name = row['department_name']

                all_employees.append(employee)

        template = 'employees/employees_list.html'
        context = {
            'employees': all_employees
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                INSERT INTO coastalapp_employee
                (
                    first_name, last_name, start_date, is_supervisor, department_id
                    )
                VALUES (?, ?, ?, ?, ?)
                """,
                              (form_data['first_name'], form_data['last_name'], form_data['start_date'], form_data['is_supervisor'], form_data["department_id"]))

            return redirect(reverse('coastalapp:employee_list'))