import sqlite3
from django.shortcuts import render
from coastalapp.models import TrainingProgram
from .job_details import get_job
from ..connection import Connection

def training_form(request):
    if request.method == 'GET':
        template = 'jobs/job_form.html'

        return render(request, template)


def training_edit_form(request, job_id):

    if request.method == "GET":
        job = get_job(job_id)

        template = 'jobs/job_form.html'

        return render(request, template, {'job': job})