from django.contrib import admin
from .models import Department, Vehicle, Employee

admin.site.register(Employee)
admin.site.register(Vehicle)
admin.site.register(Department)

