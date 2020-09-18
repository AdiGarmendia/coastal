import sqlite3
from django.shortcuts import render, reverse, redirect
from coastalapp.models import Employee
from ..connection import Connection


# def get_employee(employee_id):
#     with sqlite3.connect(Connection.db_path) as conn:
#         conn.row_factory = sqlite3.Row

#         db_cursor = conn.cursor()
#         db_cursor.execute("""
#         SELECT
#             e.id,
#             e.first_name,
#             e.last_name,
#             e.start_date,
#             e.is_supervisor,
#             e.department_id,
#             d.id department_id,
#             d.department_name
#         FROM coastalapp_employee e
#         JOIN coastalapp_department d ON e.department_id = d.id
#         WHERE e.id = ?
#         """, (employee_id,))

#         return db_cursor.fetchone()



def employee_details(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if request.method == "GET":
        template = "employees/employee_details.html"

        return render(request, template, {"employee": employee})

    elif request.method == 'POST':
        form_data = request.POST
        print(form_data["actual_method"])
        if (
            "actual_method" in form_data and form_data["actual_method"] == "PUT"
        ):
            form_data = request.POST
            print("suncess")
            employee.first_name = form_data['first_name']
            employee.last_name = form_data['last_name']
            employee.is_supervisor = form_data['is_supervisor']
            employee.department_id = form_data['department_id']
            employee.save()

        elif (
            "actual_method" in form_data and form_data["actual_method"] == "DELETE"
        ):
            employee.delete()
            return redirect(reverse('coastalapp:employee_list'))

            

        return redirect(reverse('coastalapp:employee', args=[employee_id]))