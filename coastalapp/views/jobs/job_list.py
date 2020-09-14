import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
import datetime
from coastalapp.models import Job
from ..connection import Connection


def job_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                j.id,
                j.title,
                j.start_date,
                j.completion_date,
            from coastalapp_job j
            where j.start_date >= CURRENT_DATE
            """)

            all_jobs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                job = Job()
                job.id = row['id']
                job.title = row['title']
                job.start_date = row['start_date']
                job.completion_date = row['completion_date']

                all_jobs.append(job)

        template = 'jobs/job_list.html'
        context = {
            'jobs': all_jobs
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO coastalapp_Job
            (
                title, start_date, completion_date,
            )
            VALUES (?, ?, ?, ?)
            """,
                              (form_data['title'], form_data['start_date'], form_data['completion_date'], form_data['max_capacity']))

        return redirect(reverse('coastalapp:job_list'))