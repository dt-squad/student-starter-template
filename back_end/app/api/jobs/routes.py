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
    try:
        if request.id:
            job = job_service_instance.read_job(request.id)
            return dict(job=job, message="Job found", rc=0)
    except:
        return dict(message="Job not found.", rc=16)


class Read_Job_All_Request(BaseModel):
    job_number: Optional[str] = None
    address: Optional[str] = None
    postcode: Optional[str] = None
    complaint_id: Optional[UUID] = None

@router.post("/read_all")
def read_job_all(request: Read_Job_All_Request):
    try:
        jobs = job_service_instance.read_job_all(
            request.job_number, request.address, request.postcode, request.complaint_id
        )
        return dict(jobs=jobs, message="Jobs loaded successfully.", rc=0)
    except:
        return dict(message="Failed to load jobs", rc=16)


class Update_Job_Request(BaseModel):
    id: UUID
    job_number: Optional[str] = None
    address: Optional[str] = None
    postcode: Optional[str] = None
    complaint_id: Optional[UUID] = None

@router.post("/update")
def update_job(request: Update_Job_Request):
    try:
        result = job_service_instance.update_job(
            id=request.id,
            job_number=request.job_number,
            address=request.address,
            postcode=request.postcode,
            complaint_id=request.complaint_id
        )
        return dict(result=result, message="Job updated successfully", rc=0)
    except:
        return dict(message="Job failed to update", rc=16)



class Delete_Job_Request(BaseModel):
    id: str

@router.post("/delete")
def delete_job(request:Delete_Job_Request):
    try:
        job = job_service_instance.delete_job(request.id)
        return dict(job=job, message="Job Deleted successfully", rc=0)
    except:
        return dict(message="Failed deleting job", rc=16)



class Create_Job_Stage_Request(BaseModel):
    title: str
    for_scaffold: bool

@router.post("/create_stage")
def create_job_stage(request:Create_Job_Stage_Request):
    try:
        job_stage = job_service_instance.create_job_stage(request.title, request.for_scaffold)
        return dict(job_stage=job_stage, message="Job stage created successfully", rc=0)
    except:
        return dict(message="Failed to create job stage", rc=16)


class Read_Job_Stage_Request(BaseModel):
    id: str

@router.post("/read_stage")
def read_job_stage(request:Read_Job_Stage_Request):
    try:
        job_stage = job_service_instance.read_job_stage(request.id)
        return dict(job_stage=job_stage, message="Job stage loaded successfully", rc=0)
    except:
        return dict(message="Failed to load job stage", rc=16)


class Read_Job_Stage_All_Request(BaseModel):
    title: str
    for_scaffold: bool

@router.post("/read_stage_all")
def read_job_stage_all(request:Read_Job_Stage_All_Request):
    try:
        job_stage_all = job_service_instance.read_job_stage_all(request.title, request.for_scaffold)
        return dict(job_stage=job_stage_all, message="All job stages loaded successfully", rc=0)
    except:
        return dict(message="Failed to load all job stages", rc=16)


class Update_Job_Stage_Request(BaseModel):
    id: str
    title: str
    for_scaffold: bool

@router.post("/update_stage")
def update_stage_job(request:Update_Job_Stage_Request):
    try:
        job_stage = job_service_instance.update_job_stage(request.id, request.title, request.for_scaffold)
        return dict(job_stage=job_stage, message="Job stage updated successfully", rc=0)
    except:
        return dict(message="Failed to update job stage", rc=16)


class Delete_Job_Stage_Request(BaseModel):
    id: str

@router.post("/delete_stage")
def delete_job(request:Delete_Job_Stage_Request):
    try:
        job_stage = job_service_instance.delete_job_stage(request.id)
        return dict(job_stage=job_stage, message="Job stage deleted successfully", rc=0)
    except:
        return dict(message="Failed to delete job stage", rc=16)



class Create_Job_Stage_History_Request(BaseModel):
    job_id: UUID
    stages_id: UUID
    date: str

@router.post("/create_stage_history")
def create_job_stage_history(request:Create_Job_Stage_History_Request):
    try:
        job_stage_history = job_service_instance.create_job_stage_history(request.job_stage_history_id, request.job_id, request.stages_id, request.date)
        return dict(job_stage_history=job_stage_history, message="Job stage history created successfully", rc=0)
    except:
        return dict(message="Failed to create job stage history", rc=16)


class Read_Job_Stage_History_Request(BaseModel):
    id: str

@router.post("/read_stage_history")
def read_job_stage_history(request:Read_Job_Stage_History_Request):
    try:
        job_stage_history = job_service_instance.read_job_stage_history(request.id)
        return dict(job_stage_history=job_stage_history, message="Job stage history loaded successfully", rc=0)
    except:
        return dict(message="Failed to load job stage history", rc=16)


class Read_Job_Stage_History_All_Request(BaseModel):
    job_id: UUID
    stages_id: UUID
    date: str

@router.post("/read_all_stage_history")
def read_job_stage_history_all(request:Read_Job_Stage_History_All_Request):
    try:
        job_stage_history_all = job_service_instance.read_job_stage_history_all(request.job_id, request.stages_id, request.date)
        return dict(job_stage_history=job_stage_history_all, message="All job stage history loaded successfully", rc=0)
    except:
        return dict(message="Failed to load all job stage history", rc=16)


class Update_Job_Stage_History_Request(BaseModel):
    id: UUID
    job_id: UUID
    stages_id: UUID
    date: str

@router.post("/update_stage_history")
def update_job_stage_history(request:Update_Job_Stage_History_Request):
    try:
        job_stage_history_all = job_service_instance.update_job_stage_history(request.id, request.job_number, request.address, request.postcode, request.complaint_id)
        return dict(job_stage_history=job_stage_history_all, message="Job stage history updated successfully", rc=0)
    except:
        return dict(message="Failed to update job stage history", rc=16)


class Delete_Job_Stage_History_Request(BaseModel):
    id: UUID

@router.post("/delete_stage_history")
def delete_job_stage_history(request:Delete_Job_Stage_History_Request):
    try:
        job_stage_history_all = job_service_instance.delete_job_stage_history(request.id)
        return dict(job_stage_history=job_stage_history_all, message="Job stage history deleted successfully", rc=0)
    except:
        return dict(message="Failed to deleted job stage history", rc=16)



