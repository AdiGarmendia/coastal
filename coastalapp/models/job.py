from django.db import models
from .employee import Employee


class Job(models.Model):

    
    title = models.CharField(max_length=100)
    start_date = models.DateField(null=True, auto_now=False, auto_now_add=False)
    end_date = models.DateField(null=True, auto_now=False, auto_now_add=False)
    assigned_employee = models.ForeignKey(Employee,
                                   related_name="assigned_employees",
                                   null=True,  # Makes column nullable in DB
                                   blank=True,  # Allows blank value on objects
                                   on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("Job")
        verbose_name_plural = ("Jobs")