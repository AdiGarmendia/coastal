from django.db import models
from .employee import Employee
from .vehicle import Vehicle


class EmployeeVehicle(models.Model):
    

    employee = models.ForeignKey(Employee,
                                 related_name="EmployeeVehicles",
                                 null=True,  # Makes column nullable in DB
                                 blank=True,  # Allows blank value on objects
                                 on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle,
                                 related_name="EmployeesVehicle",
                                 null=True,  # Makes column nullable in DB
                                 blank=True,  # Allows blank value on objects
                                 on_delete=models.CASCADE)
    assigned_date = models.DateField(
        null=True, auto_now=False, auto_now_add=False)
    unassigned_date = models.DateField(
        null=True, auto_now=False, auto_now_add=False)