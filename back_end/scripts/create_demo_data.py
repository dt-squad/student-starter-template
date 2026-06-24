"""
Adding random auto created DB rows

Usage: 
"""
import random
import sys
from pathlib import Path
import secrets
# Project root on path so back_end imports work when run as a script
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from back_end.database.database import SessionLocal
from back_end.database.models import Jobs, Job_Stages, Job_Stages_History, resource, Scaffold_Requests, scaffold_stage

addresses = [
    "Test Street",
    "Test Road",
    "Test Avenue",
    "Test Lane"
]

def create_resources(db):
    number_of_resouces = 40
    list_of_resources = []
    for resource_number in range(number_of_resouces):
        new_resource_record = resource(

        )
        db.add(new_resource_record)
        db.commit()
        list_of_resources.append(new_resource_record)
    
    return list_of_resources

def main(db, number_of_jobs=1000):
    list_of_resources = create_resources(db)
    for job_number in range(number_of_jobs):
        new_job_record = Jobs(
            job_number=f"RBK-{secrets.token_urlsafe(6)}",
            address=random.choice(addresses),
            post_code=f"TE57 {secrets.token_urlsafe(3)}"
        )
        db.add(new_job_record)
        db.commit()

        new_scaffold_request_record = Scaffold_Requests(
            job_id=new_job_record.id,
            use="inspection",
            status=scaffold_stage.FRONT,
            resource_id=random.choice(list_of_resources).id
        )

    
if __name__ == "__main__":
    NUMBER_OF_JOBS = 1000
    db = SessionLocal()
    main(db, NUMBER_OF_JOBS)