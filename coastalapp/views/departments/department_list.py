import sqlite3
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from coastalapp.models import Department, Employee
from ..connection import Connection


def create_departmant(cursor, row):
    _row = sqlite3.Row(cursor, row)

    department = Department()
    department.id = _row['id']
    department.department_name = _row['department_name']

    department.employees = []

    employee = Employee()
    employee.id = _row["id"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]
    employee.start_date = _row["start_date"]
    employee.is_supervisor = _row["is_supervisor"]
    employee.department_id = _row["department_id"]

    return (department, employee,)


def department_list(request):
    if request.method == 'GET':
        # with sqlite3.connect(Connection.db_path) as conn:
        #     conn.row_factory = create_departmant
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     select
        #         d.id,
        #         d.department_name,
        #         e.department_id,
        #         e.first_name,
        #         e.last_name,
        #         e.start_date,
        #         e.is_supervisor
        #     from coastalapp_department d
        #     left join coastalapp_employee e ON e.department_id = d.id
        #     """)

        #     dataset = db_cursor.fetchall()

        #     all_departments = {}

        #     for (department, employee) in dataset:
        #         if department.id not in all_departments:
        #             all_departments[department.id] = department
        #             if employee.department_id != None:
        #                 all_departments[department.id].employees.append(
        #                     employee)
        #         else:
        #             all_departments[department.id].employees.append(employee)
        all_departments = Department.objects.all()
        template = 'departments/department_list.html'
        context = {
            'all_departments': all_departments.values()
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # with sqlite3.connect(Connection.db_path) as conn:
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #         INSERT INTO coastalapp_department
        #         (
        #             department_name
        #             )
        #         VALUES (?)
        #         """,
        #                       (form_data['department_name']))

        new_department = Department()
        new_department.department_name = form_data['department_name']
        new_department.save()

        return redirect(reverse('coastalapp:department_list'))