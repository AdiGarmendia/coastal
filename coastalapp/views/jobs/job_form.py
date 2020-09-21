import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from coastalapp.models import Job
from coastalapp.models import Employee
from ..connection import Connection

@login_required
def job_form(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        template = 'jobs/job_form.html'
        context = {
            'all_employees': employees
        }

        return render(request, template, context)

def job_edit_form(request, job_id):

    if request.method == 'GET':
        job = Job.objects.get(pk=job_id)
        employees = Employee.objects.all()

        template = 'jobs/job_form.html'
        context = {
            'job': job,
            'all_employees': employees
        }

        return render(request, template, context)