from typing import Optional
from fastapi import APIRouter
from back_end.business_objects.complaints_service import Complaint_Service
from pydantic import BaseModel
from uuid import UUID

router = APIRouter()
complaint_service_instance = Complaint_Service(

)

class Create_Complaint_Request(BaseModel):
    complaint_number: str
    stage: Optional[str]

@router.post("/complaint/create")
def create_complaint(request:Create_Complaint_Request):
    complaint = Complaint_Service.create_complaint(request.complaint_number, request.stage)
    return complaint


class Read_Complaint_Request(BaseModel):
    id: str

@router.post("/complaint/read")
def read_complaint(request:Read_Complaint_Request):
    complaint = Complaint_Service.read_complaint(request.id)
    return complaint

# DOES THIS NOT NEED A CLASS???
    # complaints_service.py
    # def read_complaint_all (self):
    #     with get_db_context() as db:
    #         complaints = db.query(Complaint)

    #         return complaints

@router.post("/complaint/read_all")
def read_complaint_all(request):
    complaint = Complaint_Service.read_complaint_all(request)
    return complaint


class Update_Complaint_Request(BaseModel):
    id: str
    complaint_number: Optional[str]
    stage: Optional[str]

@router.post("/complaint/update")
def update_complaint(request:Update_Complaint_Request):
    complaint = Complaint_Service.read_complaint_all(request.id, request.complaint_number, request.address, request.postcode, request.complaint_id)
    return complaint


class Delete_Complaint_Request(BaseModel):
    id: str

@router.post("/complaint/delete")
def delete_complaint(request:Delete_Complaint_Request):
    complaint = Complaint_Service.delete_complaint(request.id)
    return complaint