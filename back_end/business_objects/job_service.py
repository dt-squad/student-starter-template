from back_end.database.models import Job, Job_Stage, Job_Stages_History
from back_end.database.database import get_db_context

class Job_Service:
    def __init__(self):
        pass

    def create_job(self, job_number, address, postcode, complaint_id=None):
        with get_db_context() as db:
            new_job = Job(
                job_number = job_number,
                address = address,
                postcode = postcode,
                complaint_id = complaint_id
            )
            db.add(new_job)
            db.commit()
            new_job_id = str(new_job.id)
            return new_job_id
        
    def read_job(self, job_id):
        with get_db_context() as db:
            job = db.query(Job).get(job_id)
            return job

    def read_job_all(self, job_number=None, address=None, postcode=None, complaint_id=None):
        with get_db_context() as db:
            jobs = db.query(Job)
            if job_number:
                jobs = jobs.filter(Job.job_number == job_number)
            if address:
                jobs = jobs.filter(Job.address == address)
            if postcode:
                jobs = jobs.filter(Job.postcode == postcode)
            if complaint_id:
                jobs = jobs.filter(Job.complaint_id == complaint_id)

            return [
                {
                    "id": str(job.id),
                    "job_number": job.job_number,
                    "address": job.address,
                    "postcode": job.postcode,
                    "complaint_id": str(job.complaint_id) if job.complaint_id else None,
                }
                for job in jobs.all()
            ]
            

    def update_job(self, id, job_number=None, address=None, postcode=None, complaint_id=None):
        with get_db_context() as db:
            job = db.query(Job).get(id)
            if id:
                if job_number:
                    job.job_number = job_number

                if address:
                    job.address = address

                if postcode:
                    job.postcode = postcode

                if complaint_id:
                    job.complaint_id = complaint_id
            else:
                return "no ID"
            db.commit()
            return True


    def delete_job(self, id):
        with get_db_context() as db:
            job = db.query(Job).get(id)

            db.delete(job)
            db.commit()
            return True
        
    def create_job_stage(self, title, for_scaffold=False):
        with get_db_context() as db:
            new_job_stage = Job_Stage(
                title = title,
                for_scaffold = for_scaffold
            )

            db.add(new_job_stage)
            db.commit

            new_job_stage_id = str(new_job_stage.id)
            return new_job_stage_id
        
    def read_job_stage_all(self):
        with get_db_context() as db:
            job_stages = db.query(Job_Stage)
            return job_stages

    def update_job_stage(self, stage_id, title=None, for_scaffold=None):
        with get_db_context() as db:
            if stage_id:
                stage = db.query(Job_Stage).get(stage_id)
                if title:
                    stage.title = title
                if for_scaffold:
                    stage.for_scaffold = for_scaffold

                db.commit()
                return True

    def delete_job_stage(self, stage_id):
        with get_db_context() as db:
            job_stage = db.query(Job_Stage).get(stage_id)

            db.delete(job_stage)
            db.commit
            return True

    def create_job_stage_history(self, job_id, stages_id):
        with get_db_context() as db:
            new_job_stage_history = Job_Stages_History(
                job_id = job_id,
                stages_id = stages_id
            )

            db.add(new_job_stage_history)
            db.commit

            new_job_stage_id = str(new_job_stage_history.id)
            return new_job_stage_id
        
    def read_job_stage_history_log(self, job_stage_history_id):
        with get_db_context() as db:
            if job_stage_history_id:
                history_log = db.query(Job_Stages_History).get(job_stage_history_id)
                return history_log

    def read_job_stage_history_job(self, job_id):
        if not job_id:
            return []
            
        with get_db_context() as db:
            return db.query(Job_Stages_History).filter(Job_Stages_History.job_id == job_id).all()
        
    def read_job_stage_history_all(self):
        with get_db_context() as db:
            return db.query(Job_Stages_History)

    def update_job_stage_history(self, job_stage_history_id, job_id=None, stages_id=None, date=None):
        with get_db_context() as db:
            if job_stage_history_id:
                log = db.query(Job_Stages_History).get(job_stage_history_id)
                if job_id:
                    log.job_id = job_id
                if stages_id:
                    log.stages_id = stages_id
                if date:
                    log.date = date
                
                db.commit()
                return True


    def delete_job_stage_history(self, job_stage_history_id):
        with get_db_context() as db:
            if job_stage_history_id:
                log = db.query(Job_Stages_History).get(job_stage_history_id)
                db.delete(log)
                db.commit()
                return True
            

if __name__ == "__main__":
    job_service = Job_Service()
    id = job_service.create_job("RBK-589455", "23 Test Street", "TE57G56")
    job_service.update_job(id, complaint_id="708d0b90-5836-4dfb-a115-e9abf89d069c")
    print(id)
