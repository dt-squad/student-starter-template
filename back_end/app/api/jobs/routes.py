from typing import Optional
from fastapi import APIRouter, Request
from back_end.business_objects.job_service import Job_Service
from pydantic import BaseModel
from uuid import UUID

router = APIRouter()
job_service_instance = Job_Service(

)

class Create_Job_Request(BaseModel):
    job_number: str
    address: Optional[str]
    postcode: Optional[str]
    complaint_id: Optional[UUID]

@router.post("/api/job/create/")
async def create_job(request: Request):
    new_job = await request.json()
    print(new_job)
    job = Job_Service.create_job(new_job["job_number"], new_job["address"], new_job["postcode"], new_job["complaint_id"])
    return job


class Read_Job_Request(BaseModel):
    id: str

@router.post("/api/job/read/")
def read_job(request:Read_Job_Request):
    job = Job_Service.read_job(request.id)
    return job


class Read_Job_All_Request(BaseModel):
    job_number: Optional[str]
    address: Optional[str]
    postcode: Optional[str]
    complaint_id: Optional[UUID]

@router.post("/api/job/read_all/")
def read_job_all(request:Read_Job_All_Request):
    job = Job_Service.read_job_all(request.job_number, request.address, request.postcode, request.complaint_id)
    return job


class Update_Job_Request(BaseModel):
    id: str
    job_number: Optional[str]
    address: Optional[str]
    postcode: Optional[str]
    complaint_id: Optional[UUID]

@router.post("/api/job/update_all/")
def update_job(request:Update_Job_Request):
    job = Job_Service.read_job_all(request.id, request.job_number, request.address, request.postcode, request.complaint_id)
    return job


class Delete_Job_Request(BaseModel):
    id: str

@router.post("/api/job/delete_all/")
def delete_job(request:Delete_Job_Request):
    job = Job_Service.delete_job(request.id)
    return job



class Create_Job_Stage_Request(BaseModel):
    title: str
    for_scaffold: bool

@router.post("/job/create_stage")
def create_job_stage(request:Create_Job_Stage_Request):
    job = Job_Service.create_job_stage(request.title, request.for_scaffold)
    return job


class Read_Job_Stage_Request(BaseModel):
    id: str

@router.post("/job/read_stage")
def read_job_stage(request:Read_Job_Stage_Request):
    job = Job_Service.read_job_stage(request.id)
    return job


class Read_Job_Stage_All_Request(BaseModel):
    title: str
    for_scaffold: bool

@router.post("/job/read_stage_all")
def read_job_stage_all(request:Read_Job_Stage_All_Request):
    job = Job_Service.read_job_stage_all(request.title, request.for_scaffold)
    return job


class Update_Job_Stage_Request(BaseModel):
    id: str
    title: str
    for_scaffold: bool

@router.post("/job/update_stage")
def update_stage_job(request:Update_Job_Stage_Request):
    job = Job_Service.update_job_stage(request.id, request.title, request.for_scaffold)
    return job


class Delete_Job_Stage_Request(BaseModel):
    id: str

@router.post("/job/delete_stage")
def delete_job(request:Delete_Job_Stage_Request):
    job = Job_Service.delete_job_stage(request.id)
    return job



class Create_Job_Stage_History_Request(BaseModel):
    job_id: UUID
    stages_id: UUID
    date: str

@router.post("/job/create_stage_history")
def create_job_stage_history(request:Create_Job_Stage_History_Request):
    job = Job_Service.create_job_stage_history(request.job_stage_history_id, request.job_id, request.stages_id, request.date)
    return job


class Read_Job_Stage_History_Request(BaseModel):
    id: str

@router.post("/job/read_stage_history")
def read_job_stage_history(request:Read_Job_Stage_History_Request):
    job = Job_Service.read_job_stage_history(request.id)
    return job


class Read_Job_Stage_History_All_Request(BaseModel):
    job_id: UUID
    stages_id: UUID
    date: str

@router.post("/job/read_all_stage_history")
def read_job_stage_history_all(request:Read_Job_Stage_History_All_Request):
    job = Job_Service.read_job_stage_history_all(request.job_id, request.stages_id, request.date)
    return job


class Update_Job_Stage_History_Request(BaseModel):
    id: UUID
    job_id: UUID
    stages_id: UUID
    date: str

@router.post("/job/update_stage_history")
def update_job_stage_history(request:Update_Job_Stage_History_Request):
    job = Job_Service.update_job_stage_history(request.id, request.job_number, request.address, request.postcode, request.complaint_id)
    return job


class Delete_Job_Stage_History_Request(BaseModel):
    id: UUID

@router.post("/job/delete_stage_history")
def delete_job_stage_history(request:Delete_Job_Stage_History_Request):
    job = Job_Service.delete_job_stage_history(request.id)
    return job



