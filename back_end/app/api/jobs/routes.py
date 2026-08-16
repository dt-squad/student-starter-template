from typing import Optional
from fastapi import APIRouter, Request
from back_end.business_objects.job_service import Job_Service
from pydantic import BaseModel
from uuid import UUID

router = APIRouter()
job_service_instance = Job_Service(

)

class Create_Job_Request(BaseModel):
    job_number: Optional[str] = None
    address: Optional[str] = None
    postcode: Optional[str] = None
    complaint_id: Optional[UUID] = None

@router.post("/create")
def create_job(request: Create_Job_Request):
    try:
        job = job_service_instance.create_job(
            job_number=request.job_number,
            address=request.address,
            postcode=request.postcode,
            complaint_id=request.complaint_id
        )
        return dict(job=job, message="Job Created Successfully", rc=0)
    except:
        return dict(message="Job creation failed", rc=16)


class Read_Job_Request(BaseModel):
    id: str

@router.post("/read")
def read_job(request:Read_Job_Request):
    if request.id:
        job = Job_Service.read_job(request.id)
        return job
    else:
        return "Job not found."


class Read_Job_All_Request(BaseModel):
    job_number: Optional[str] = None
    address: Optional[str] = None
    postcode: Optional[str] = None
    complaint_id: Optional[UUID] = None

@router.post("/read_all")
def read_job_all(request: Read_Job_All_Request):
    jobs = job_service_instance.read_job_all(
        request.job_number, request.address, request.postcode, request.complaint_id
    )
    return jobs


class Update_Job_Request(BaseModel):
    id: UUID
    job_number: Optional[str] = None
    address: Optional[str] = None
    postcode: Optional[str] = None
    complaint_id: Optional[UUID] = None

@router.post("/update")
def update_job(request: Update_Job_Request):
    result = job_service_instance.update_job(
        id=request.id,
        job_number=request.job_number,
        address=request.address,
        postcode=request.postcode,
        complaint_id=request.complaint_id
    )
    return {"success": result}


class Delete_Job_Request(BaseModel):
    id: str

@router.post("/delete")
def delete_job(request:Delete_Job_Request):
    job = job_service_instance.delete_job(request.id)
    return job



class Create_Job_Stage_Request(BaseModel):
    title: str
    for_scaffold: bool

@router.post("/create_stage")
def create_job_stage(request:Create_Job_Stage_Request):
    job = Job_Service.create_job_stage(request.title, request.for_scaffold)
    return job


class Read_Job_Stage_Request(BaseModel):
    id: str

@router.post("/read_stage")
def read_job_stage(request:Read_Job_Stage_Request):
    job = Job_Service.read_job_stage(request.id)
    return job


class Read_Job_Stage_All_Request(BaseModel):
    title: str
    for_scaffold: bool

@router.post("/read_stage_all")
def read_job_stage_all(request:Read_Job_Stage_All_Request):
    job = Job_Service.read_job_stage_all(request.title, request.for_scaffold)
    return job


class Update_Job_Stage_Request(BaseModel):
    id: str
    title: str
    for_scaffold: bool

@router.post("/update_stage")
def update_stage_job(request:Update_Job_Stage_Request):
    job = Job_Service.update_job_stage(request.id, request.title, request.for_scaffold)
    return job


class Delete_Job_Stage_Request(BaseModel):
    id: str

@router.post("/delete_stage")
def delete_job(request:Delete_Job_Stage_Request):
    job = Job_Service.delete_job_stage(request.id)
    return job



class Create_Job_Stage_History_Request(BaseModel):
    job_id: UUID
    stages_id: UUID
    date: str

@router.post("/create_stage_history")
def create_job_stage_history(request:Create_Job_Stage_History_Request):
    job = Job_Service.create_job_stage_history(request.job_stage_history_id, request.job_id, request.stages_id, request.date)
    return job


class Read_Job_Stage_History_Request(BaseModel):
    id: str

@router.post("/read_stage_history")
def read_job_stage_history(request:Read_Job_Stage_History_Request):
    job = Job_Service.read_job_stage_history(request.id)
    return job


class Read_Job_Stage_History_All_Request(BaseModel):
    job_id: UUID
    stages_id: UUID
    date: str

@router.post("/read_all_stage_history")
def read_job_stage_history_all(request:Read_Job_Stage_History_All_Request):
    job = Job_Service.read_job_stage_history_all(request.job_id, request.stages_id, request.date)
    return job


class Update_Job_Stage_History_Request(BaseModel):
    id: UUID
    job_id: UUID
    stages_id: UUID
    date: str

@router.post("/update_stage_history")
def update_job_stage_history(request:Update_Job_Stage_History_Request):
    job = Job_Service.update_job_stage_history(request.id, request.job_number, request.address, request.postcode, request.complaint_id)
    return job


class Delete_Job_Stage_History_Request(BaseModel):
    id: UUID

@router.post("/delete_stage_history")
def delete_job_stage_history(request:Delete_Job_Stage_History_Request):
    job = Job_Service.delete_job_stage_history(request.id)
    return job



