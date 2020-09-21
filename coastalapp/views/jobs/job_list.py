import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
import datetime
from coastalapp.models import Job
from ..connection import Connection


def job_list(request):
    if request.method == 'GET':
        all_jobs = Job.objects.all()
        template = 'jobs/job_list.html'
        context = {
            'jobs': all_jobs
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_job = Job()
        new_job.title = form_data['title']
        new_job.start_date = form_data['start_date']
        new_job.end_date = form_data['end_date']
        new_job.save()

        return redirect(reverse('coastalapp:job_list'))