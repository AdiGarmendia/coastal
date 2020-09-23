import sqlite3
from datetime import datetime
from django.shortcuts import render, reverse, redirect
from coastalapp.models import Job
from coastalapp.models import EmployeeJob
from ..connection import Connection

def job_details(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == "GET":
        template = "jobs/job_details.html"

        return render(request, template, {"job": job})

    elif request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data and form_data["actual_method"] == "PUT"
        ):
            employeejob = EmployeeJob()
            employeejob.employee_id = form_data['employee_id']
            employeejob.job_id = Job.objects.get(pk=job_id).id
            employeejob.assigned_date = datetime.now().date()
            employeejob.save()

        elif (
            "actual_method" in form_data and form_data["actual_method"] == "DELETE"
        ):
            job.delete()
            return redirect(reverse('coastalapp:job_list'))

            

        return redirect(reverse('coastalapp:job', args=[job_id]))