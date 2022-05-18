# todas as rotas relacionadas a jobs e vai redirecionar para o model especifico
# (não coloca regra de negocio/lógica)
from flask import Blueprint
from model.create_job import create_job
from model.get_job import get_job
import json
from flask import request
from dto.job import Job


jobs_blueprint = Blueprint("jobs", __name__)


@jobs_blueprint.route("/jobs", methods=["POST"])
def create_job_controller():
    try:
        input_json = request.get_json(force=True)
        jobs = []

        if not (type(input_json["jobs"]) is list):
            return "The type is not JSON"

        for item in input_json["jobs"]:
            job = Job(
                title=item["title"],
                apply_url=item["apply_url"],
                department=item["department"],
                location=item["location"],
                description=item["description"],
                created_on=item["created_on"],
            )
            jobs.append(job)

        create_job(jobs)
        return "A Job was sucessfully submitted!"

    except Exception as e:
        print(e)
        return "Backend error!"


@jobs_blueprint.route("/jobs", methods=["GET"])
def get_job_list_controller():
    try:
        result = get_job()
        return json.dumps(result)

    except Exception as e:
        print(e)
        print("An GET error had occured")
