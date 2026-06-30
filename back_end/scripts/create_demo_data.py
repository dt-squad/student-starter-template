"""
Adding random auto created DB rows

Usage: 
"""
import random
import sys
from pathlib import Path
import secrets
from datetime import datetime, timedelta
from lorem_text import lorem

# Project root on path so back_end imports work when run as a script
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from back_end.database.database import SessionLocal
from back_end.database.models import (
    ComplaintStages, 
    Complaint, 
    Job,
    Job_Stage,
    Job_Stages_History,
    Resource,
    Resource_Contact,
    Resource_Trade,
    Scaffold_Request,
    Scaffold_Stages,
    Scaffold_Elevations,
    Scaffold_Elevation,
    Scaffold_Checklist_Item,
    Scaffold_Media_Types,
    Scaffold_Media
)  

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

first_names = [
    "Oliver", "George", "Noah", "Arthur", "Leo", "Oscar", "Harry", "Archie", "Jack", "Henry",
    "Charlie", "Thomas", "William", "Teddy", "Lucas", "James", "Freddie", "Theo", "Isaac", "Alfie",
    "Olivia", "Amelia", "Isla", "Ava", "Ivy", "Freya", "Lily", "Florence", "Mia", "Willow",
    "Rosie", "Sophia", "Isabella", "Grace", "Daisy", "Sienna", "Poppy", "Harper", "Emily", "Ella",
    "Edward", "Joseph", "Samuel", "Benjamin", "Max", "Mohammed", "Finley", "Louie", "Evie", "Elsie"
]

last_names = [
    "Smith", "Jones", "Taylor", "Brown", "Williams", "Wilson", "Johnson", "Davies", "Robinson", "Wright",
    "Thompson", "Evans", "Walker", "White", "Roberts", "Green", "Hall", "Wood", "Jackson", "Clarke",
    "Hughes", "Edwards", "Turner", "Lewis", "Hill", "Harris", "Martin", "Cooper", "Harrison", "Ward",
    "Baker", "Morris", "Morgan", "King", "Allen", "Carter", "James", "Watson", "Brooks", "Bennett",
    "Gray", "Price", "Hamilton", "Wallace", "Cole", "Rowe", "Fox", "Bell", "Chapman", "Hunt"
]

def create_resource_trades(db):
    list_of_trades = []
    trades = [
        "Carpentry",
        "Groundsworking",
        "Electrics",
        "Drainage",
        "Roofing",
        "Scaffolding",
        "Plumbing",
        "Pest-Control",
        "Environmental Cleaning"
    ]

    for trade_num in len(trades):
        trade = trades[trade_num]
        new_resource_trade = Resource_Trade(
            trade = trade
        )
        db.add(new_resource_trade)
        db.commit()
        list_of_trades.append(new_resource_trade)
    
    return list_of_trades

def create_resource_name(subcontractor_boolean, first, last, trades):
    if subcontractor_boolean:
        return first[0] + "." + last[0] + " ", random.choice(trades)
    else:
        return first + " " + last

def random_boolean():
    rand = random.randrange(1,2)
    if rand == 1:
        return True
    else:
        return False

def create_email(first, last, resource_name):
    email = first + "." + last + "@" + resource_name.replace(" ", "") + ".co.uk"
    return


def create_resources(db):
    number_of_resouces = 40
    list_of_resources = []
    list_of_trades = create_resource_trades(db)
    for resource_number in range(number_of_resouces):
        first = random.choice(first_names)
        last = random.choice(last_names)
        subcontractor_boolean = random_boolean()

        new_resource_record = Resource(
            name = create_resource_name(subcontractor_boolean, first, last, list_of_trades),
            subcontractor = subcontractor_boolean
        )
        db.add(new_resource_record)
        db.commit()
        list_of_resources.append(new_resource_record)

        role_choices = [
            "Director",
            "Admin",
            "Manager",
            "Supervisor"
        ]

        if new_resource_record.subcontractor:
            for resource_contact in range(random.randrange(1, 3)):
                new_resource_contact_record = Resource_Contact(
                    resource_id = new_resource_record.id,
                    name = first + last,
                    email = create_email(first, last, new_resource_record.name)
                    phone = "+447" + random.randint(100000000, 999999999)
                    role = random.choice(role_choices)
                )
                db.add(new_resource_contact_record)
                db.commit
    
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
    number_of_complaints = number_of_jobs / 10

    list_of_resources = create_resources(db)
    list_of_job_stages = create_job_stages(db)

    for job_number in range(number_of_jobs):
        num_stages_completed = random.randint(1, len(list_of_job_stages))
        stages_for_this_job = list_of_job_stages[:num_stages_completed]

        new_job_record = Job(
            job_number=f"RBK-{secrets.token_urlsafe(6)}",
            address=random.choice(addresses),
            post_code=random.choice(postcodes)
        )
        db.add(new_job_record)
        db.commit() 

        current_stage_date = datetime.now() - timedelta(days=random.randint(180, 365))

        for stage_record in stages_for_this_job:
            new_job_stage_history_record = Job_Stages_History(
                job_id=new_job_record.id,
                stages_id=stage_record.id, # FIX: Accessing the ID from the record
                date=current_stage_date
            )
            db.add(new_job_stage_history_record)
            
            current_stage_date += timedelta(days=random.randint(1, 14))
            
            db.commit()

        if job_number / 10 == 1:
            new_scaffold_request_record = Scaffold_Request(
                job_id=new_job_record.id,
                use="inspection",
                status=random.choice(Scaffold_Stages)
                resource_id=random.choice(list_of_resources).id
            )
            db.add(new_scaffold_request_record)
            db.commit()

            for elevation in random.randrange(1,4):
                new_scaffold_elevation = Scaffold_Elevation(
                    scaffold_id = new_scaffold_request_record.id,
                    elevation = random.choice(Scaffold_Elevations),
                    height = random.randrange(3, 21)
                    width = random.randrange(4, 30),
                    chimney = random_boolean(),
                    notes = lorem.scentence
                )
                db.add(new_scaffold_elevation)
                db.commit()

    # Create 1 Complaint for every 10 Jobs
    for complaint_record in range(number_of_complaints):
        new_complaint_record = Complaint(
            complaint_number = f"RBK-COMP-{secrets.token_urlsafe(6)}",
            stage = random.choice(ComplaintStages)
        )
        db.add()
        db.commit()


        Scaffold_Elevations(

        )
        db.add()
        db.commit()


        Scaffold_Media(

        )
        db.add()
        db.commit()



    
if __name__ == "__main__":
    NUMBER_OF_JOBS = 1000
    db = SessionLocal()
    main(db, NUMBER_OF_JOBS)