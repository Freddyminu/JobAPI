import providers.job as jobprovider


def create_job(jobs):
    try:
        for job in jobs:
            jobprovider.create_job(job)
            print("Passou o provider")
        return True

    except Exception as e:
        print(e)
        raise Exception("Model Error in the create_job.py file!")
