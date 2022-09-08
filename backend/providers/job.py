from db import db_connection
import sys
import sqlite3 as sql
from dto.job import Job


def create_job(job: Job):
    try:
        con = db_connection()
        c = con.cursor()
        term = """
            INSERT INTO Jobs
                (title, apply_url, department,
                location, description, created_on)
            VALUES (?, ?, ?, ?, ?, ?)
            """
        c.execute(
            term,
            (
                job["title"],
                job["apply_url"],
                job["department"],
                job["location"],
                job["description"],
                job["created_on"],
            ),
        )
        print("A Job was sucessfully submitted!")
        con.commit()
        return True

    except Exception as e:
        print(e, file=sys.stderr)
        raise Exception("An SQL error has occured in the provider file")


def get_job():
    jobs = []
    try:
        con = db_connection()
        con.row_factory = sql.Row
        c = con.cursor()
        c.execute("SELECT * FROM Jobs")
        result = c.fetchall()

        for item in result:
            job = Job(
                title=item["title"],
                apply_url=item["apply_url"],
                department=item["department"],
                location=item["location"],
                description=item["description"],
                created_on=item["created_on"],
            )
            jobs.append(job)

        return jobs

    except Exception as e:
        print(e)
        print("An GET error had occured in the provider file")
