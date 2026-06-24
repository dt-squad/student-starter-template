"""
Adding random auto created DB rows

Usage: 
"""
import random

from sqlalchemy import insert

addresses = [
    "Test Street",
    "Test Road",
    "Test Avenue",
    "Test Lane"
]
   
def insert_1000_complaints():
    i = 0

    stages = [
        'Member_MP_Enquiry',
        'Stage 1',
        'Stage 2',
        'Ombudsman']

    while i < 1000:
        complaint_number="TEST-COMP-" + i
        stage = random.choice(stages)
        address = i + " " + random.choice(addresses)
        postcode = "TE57A" + i
        insert(py_complaints).values(complaint_number=complaint_number, stage=stage, address=address, postcode=postcode)
        i += 1


def insert_1000_jobs():
    i = 0
    
    while i < 1000:
        job_number = "TEST-" + i
        address = i + " " + random.choice(addresses)
        postcode = "TE57A" + i
        insert(jobs).values(job_number=job_number, address=address, postcode=postcode)
        i += 1


def insert_200_scaffold():
    i = 0

    while i < 200:
        job_id = # Needs to connect to job
        use = "Inspection"
        status = # Needs scaffold_stages
        resource_id = # Needs to connect to the resource
        insert(scaffold_requests).values(job_id=job_id, use=use, status=status, resource_id=resource_id)
        i += 1

    
if __name__ == "__main__":
    insert_1000_complaints()
    insert_1000_jobs()
    insert_200_scaffold