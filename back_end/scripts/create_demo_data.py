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
    "12 Oakwood Close, Richmond, Surrey",
    "45 Maple Avenue, Twickenham, Greater London",
    "78 Willow Road, Kingston upon Thames, Surrey",
    "23 Elm Street, Teddington, Greater London",
    "91 Birch Grove, Staines-upon-Thames, Surrey",
    "34 Cedar Way, Hounslow, Greater London",
    "56 Pine Close, Ealing, Greater London",
    "17 Sycamore Drive, Wimbledon, Greater London",
    "83 Hawthorn Lane, Croydon, Greater London",
    "29 Ash Road, Sutton, Greater London",
    "64 Beech Avenue, Guildford, Surrey",
    "38 Chestnut Court, Woking, Surrey",
    "105 Rose Gardens, Leatherhead, Surrey",
    "51 Lavender Walk, Reigate, Surrey",
    "72 Blossom Crescent, Farnham, Surrey",
    "14 Victoria Road, Reading, Berkshire",
    "88 Windsor Street, Slough, Berkshire",
    "33 Queens Avenue, Maidenhead, Berkshire",
    "57 Station Road, Bracknell, Berkshire",
    "102 Park View, Newbury, Berkshire",
    "19 Church Lane, Oxford, Oxfordshire",
    "46 Mill Road, Banbury, Oxfordshire",
    "81 High Street, Abingdon, Oxfordshire",
    "27 Meadow Close, Didcot, Oxfordshire",
    "63 Riverbank Way, Witney, Oxfordshire",
    "11 Green Lane, Cambridge, Cambridgeshire",
    "74 Orchard Road, Ely, Cambridgeshire",
    "39 Brookside, Huntingdon, Cambridgeshire",
    "95 Kingfisher Drive, Peterborough, Cambridgeshire",
    "22 Riverside Walk, St Neots, Cambridgeshire",
    "48 Albert Street, Bristol, Bristol",
    "67 Clifton Road, Bath, Somerset",
    "13 Harbour View, Weston-super-Mare, Somerset",
    "86 Hilltop Crescent, Taunton, Somerset",
    "31 Orchard Close, Yeovil, Somerset",
    "58 Market Street, Birmingham, West Midlands",
    "104 Warwick Road, Coventry, West Midlands",
    "26 Canal Side, Wolverhampton, West Midlands",
    "79 Linden Grove, Solihull, West Midlands",
    "43 Holly Road, Dudley, West Midlands",
    "15 Castle Street, Manchester, Greater Manchester",
    "92 Victoria Park Road, Salford, Greater Manchester",
    "37 King Street, Bolton, Greater Manchester",
    "61 Moorland Drive, Stockport, Greater Manchester",
    "84 Cherry Tree Lane, Wigan, Greater Manchester",
    "28 George Street, Edinburgh, Midlothian",
    "53 Princes Road, Glasgow, Lanarkshire",
    "76 Seaview Terrace, Aberdeen, Aberdeenshire",
    "41 Highfield Road, Dundee, Angus",
    "109 Harbour Road, Inverness, Highland"
]

postcodes = [
    "TW9 1AA",
    "TW1 2BB",
    "KT2 3CC",
    "TW11 4DD",
    "TW18 5EE",
    "TW3 6FF",
    "W5 7GG",
    "SW19 8HH",
    "CR0 9JJ",
    "SM1 1KK",
    "GU1 2LL",
    "GU21 3MM",
    "KT22 4NN",
    "RH2 5PP",
    "GU9 6QQ",
    "RG1 7RR",
    "SL1 8SS",
    "SL6 9TT",
    "RG12 1UU",
    "RG14 2VV",
    "OX1 3WW",
    "OX16 4XX",
    "OX14 5YY",
    "OX11 6ZZ",
    "OX28 7AB",
    "CB1 2CD",
    "CB7 3EF",
    "PE29 4GH",
    "PE1 5IJ",
    "PE19 6KL",
    "BS1 7MN",
    "BA1 8OP",
    "BS23 9QR",
    "TA1 1ST",
    "BA20 2UV",
    "B1 3WX",
    "CV1 4YZ",
    "WV1 5AB",
    "B91 6CD",
    "DY1 7EF",
    "M1 8GH",
    "M5 9IJ",
    "BL1 1KL",
    "SK1 2MN",
    "WN1 3OP",
    "EH2 4QR",
    "G1 5ST",
    "AB10 6UV",
    "DD1 7WX",
    "IV1 8YZ"
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

def create_job_stages(db):
    job_stages_names = [
        "Raised",
        "Initial Visit",
        "VO Requested",
        "VO Approved",
        "Works in progress",
        "Works Complete"
    ]
    list_of_job_stages = []
    for job_stage in job_stages_names:
        new_job_stage_record = job_stage(
            title=job_stage,
            for_scaffold=False
        )
        db.add(new_job_stage_record)
        db.commit()
        list_of_job_stages.append(new_job_stage_record)

    return list_of_job_stages


def main(db, number_of_jobs=1000):
    list_of_resources = create_resources(db)
    list_of_job_stages = create_job_stages(db)

    for job_number in range(number_of_jobs):
        new_job_record = Jobs(
            job_number=f"RBK-{secrets.token_urlsafe(6)}",
            address=random.choice(addresses),
            post_code=random.choice(postcodes)
        )
        db.add(new_job_record)
        db.commit()

        new_scaffold_request_record = Scaffold_Requests(
            job_id=new_job_record.id,
            use="inspection",
            status=scaffold_stage.FRONT,
            resource_id=random.choice(list_of_resources).id
        )
        db.add(new_scaffold_request_record)
        db.commit()

        new_complaints_record = 

    
if __name__ == "__main__":
    NUMBER_OF_JOBS = 1000
    db = SessionLocal()
    main(db, NUMBER_OF_JOBS)