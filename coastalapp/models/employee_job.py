from django.db import models
from .employee import Employee
from .job import Job


class EmployeeJob(models.Model):
    

    employee = models.ForeignKey(Employee,
                                 null=True,  # Makes column nullable in DB
                                 blank=True,  # Allows blank value on objects
                                 on_delete=models.CASCADE)
    job = models.ForeignKey(Job,
                                 null=True,  # Makes column nullable in DB
                                 blank=True,  # Allows blank value on objects
                                 on_delete=models.CASCADE)
    assigned_date = models.DateField(
        null=True, auto_now=False, auto_now_add=False)
    unassigned_date = models.DateField(
        null=True, auto_now=False, auto_now_add=False)