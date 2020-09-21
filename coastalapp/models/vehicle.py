from django.db import models
from django.urls import reverse
from .employee import Employee


class Vehicle(models.Model):
    
    manufacturer = models.CharField(null=True, max_length=50)
    make = models.CharField(max_length=20)
    purchase_date = models.DateField()
    retired_date = models.DateField(null=True, blank=True, default=None)
    employee = models.ForeignKey(Employee,
                                   related_name="employees",
                                   null=True,  # Makes column nullable in DB
                                   blank=True,  # Allows blank value on objects
                                   on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("Vehicle")
        verbose_name_plural = ("Vehicles")

    def get_absolute_url(self):
        return reverse("Vehicle_detail", kwargs={"pk": self.pk})