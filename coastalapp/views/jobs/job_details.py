import sqlite3
from django.shortcuts import render, reverse, redirect
from coastalapp.models import Job
from ..connection import Connection


def get_job(job_id):
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
            WHERE j.id = ?
            """, (job_id,))

        return db_cursor.fetchone()


def job_details(request, job_id):
    if request.method == "GET":
        job = get_job(job_id)
        template = 'jobs/job_details.html'

        return render(request, template, {"job": job})

    elif request.method == "POST":
        form_data = request.POST

        if (
            "actual_method" in form_data and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE coastalapp_job
                SET 
                    title = ?,
                    start_date = ?,
                    end_date = ?,
                WHERE id = ?
                """, (form_data['title'], form_data['start_date'], form_data['end_date'],
                      job_id))

                return redirect(reverse('coastalapp:job', args=[job_id]))

        if request.method == 'POST':
            form_data = request.POST
            

            if (
                "actual_method" in form_data
                and form_data["actual_method"] == "DELETE"
            ):
                with sqlite3.connect(Connection.db_path) as conn:
                    db_cursor = conn.cursor()

                    db_cursor.execute("""
                    DELETE FROM coastalapp_job
                    WHERE id = ?
                    """, (job_id,))

                return redirect(reverse('coastalapp:job_list'))