# aqui vc vai fazer sua lógica
import providers.job as jobprovider


def get_job():
    try:
        jobs = jobprovider.get_job()

        return jobs

    except Exception as e:
        print(e)
        raise Exception("Model Error in the get_job.py file!")
