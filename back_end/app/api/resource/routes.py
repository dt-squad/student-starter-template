from typing import Optional
from fastapi import APIRouter
from back_end.business_objects.resource_service import Resource_Service
from pydantic import BaseModel
from uuid import UUID

router = APIRouter()
resource_service_instance = Resource_Service(

)

class Create_Resource_Request(BaseModel):
    name: str
    subcontractor: bool

@router.post("/resource/create")
def create_resource(request:Create_Resource_Request):
    resource = Resource_Service.create_resource(request.name, request.subcontractor)
    return resource


class Read_Resource_Request(BaseModel):
    id: str

@router.post("/resource/read")
def read_resource(request:Read_Resource_Request):
    resource = Resource_Service.read_resource(request.id)
    return resource


class Read_Resource_All_Request(BaseModel):
    name: Optional[str]
    subcontractor: Optional[bool]

@router.post("/resource/read_all")
def read_resource_all(request:Read_Resource_All_Request):
    resource = Resource_Service.read_resource_all(request.name, request.subcontractor)
    return resource


class Update_Resource_Request(BaseModel):
    id: str
    resource_number: Optional[str]
    address: Optional[str]
    postcode: Optional[str]
    complaint_id: Optional[UUID]

@router.post("/resource/read_all")
def update_resource(request:Update_Resource_Request):
    resource = Resource_Service.read_resource_all(request.id, request.name, request.subcontractor)
    return resource


class Delete_Resource_Request(BaseModel):
    id: str

@router.post("/resource/read_all")
def delete_resource(request:Delete_Resource_Request):
    resource = Resource_Service.delete_resource(request.id)
    return resource



class Create_Resource_Contact_Request(BaseModel):
    resource_id:UUID
    name: str
    email: Optional[str]
    phone: Optional[str]
    role: Optional[str]

@router.post("/resource/create_resource_contact")
def create_resource_contact(request:Create_Resource_Contact_Request):
    resource_contact = Resource_Service.create_resource_contact(request.resource_id, request.name, request.email, request.phone, request.role)
    return resource_contact


class Read_Resource_Contact_Request(BaseModel):
    id: str

@router.post("/resource/read_resource_contact")
def read_resource_contact(request:Read_Resource_Contact_Request):
    resource_contact = Resource_Service.read_resource_contact(request.id)
    return resource_contact


class Read_Resource_Contact_All_Request(BaseModel):
    resource_id: Optional[UUID]
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    role: Optional[str]

@router.post("/resource/read_resource_contact_all")
def read_resource_contact_all(request:Read_Resource_Contact_Request):
    resource_contact = Resource_Service.read_resource_contact_all(request.resource_id, request.name, request.email, request.phone, request.role)
    return resource_contact


class Update_Resource_Contact_Request(BaseModel):
    id: UUID
    resource_id: Optional[UUID]
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    role: Optional[str]

@router.post("/resource/update_resource_contact")
def update_resource_contact(request:Update_Resource_Contact_Request):
    resource_contact = Resource_Service.update_resource_contact(request.id, request.resource_id, request.name, request.email, request.phone, request.role)
    return resource_contact


class Delete_Resource_Contact_Request(BaseModel):
    id: str

@router.post("/resource/delete_resource_contact")
def delete_resource_contact(request:Delete_Resource_Contact_Request):
    resource_contact = Resource_Service.delete_resource_contact(request.id)
    return resource_contact



class Create_Resource_Trade_Request(BaseModel):
    trade: str

@router.post("/resource/create")
def create_resource_trade(request:Create_Resource_Trade_Request):
    trade = Resource_Service.create_resource_trade(request.trade)
    return trade


class Read_Resource_Trade_Request(BaseModel):
    id: str

@router.post("/resource/read")
def read_resource_trade(request:Read_Resource_Trade_Request):
    trade = Resource_Service.read_resource_trade(request.id)
    return trade


class Read_Resource_Trade_All_Request(BaseModel):
    trade: Optional[str]

@router.post("/resource/read_all")
def read_resource_trade_all(request:Read_Resource_Trade_All_Request):
    trade = Resource_Service.read_resource_trade_all(request.trade)
    return trade


class Update_Resource_Trade_Request(BaseModel):
    id: UUID
    trade: Optional[str]

@router.post("/resource/read_all")
def update_resource_trade(request:Update_Resource_Trade_Request):
    trade = Resource_Service.update_resource_trade(request.id, request.trade)
    return trade


class Delete_Resource_Trade_History_Request(BaseModel):
    id: UUID

@router.post("/resource/read_all")
def delete_resource_trade(request:Delete_Resource_Trade_History_Request):
    trade = Resource_Service.delete_resource_trade(request.id)
    return trade



