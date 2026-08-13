from back_end.database.models import Complaint
from back_end.database.database import get_db_context

class Complaint_Service:
    def __init__(self):
        pass

    def create_complaint (self, complaint_number, stage=None):
        with get_db_context() as db:
            new_complaint = Complaint(
                complaint_number = complaint_number,
                stage = stage
            )
            db.add(new_complaint)
            db.commit()
            new_complaint_id = str(new_complaint.id)
            return new_complaint_id

    def read_complaint(self, complaint_id):
        with get_db_context() as db:
            complaint = db.query(Complaint).get(complaint_id)
            return complaint
        
    def read_complaint_all(self, complaint_id=None, complaint_number=None, stage=None):
        with get_db_context() as db:
            complaints = db.query(Complaint).all()

            return complaints
        
    def update_complaint(self, complaint_id, complaint_number=None, stage=None):
        with get_db_context() as db:
            complaint = db.query(Complaint).get(complaint_id)

            if complaint_number:
                complaint.complaint_number = complaint_number


            if stage:
                complaint.stage = stage

            db.commit()
            return True
        
    def delete_complaint(self, complaint_id):
        with get_db_context() as db:
            complaint = db.query(Complaint).get(complaint_id)
            db.delete(complaint)
            db.commit()
            return True


if __name__ == "__main__":
    complaint_service = Complaint_Service()
    id = complaint_service.create_complaint("RBK-COMP-789456", "STAGE_1")

    print(id)