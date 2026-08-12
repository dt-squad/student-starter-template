from back_end.business_objects.scaffold_service import Scaffold_Service
from typing import Optional
from fastapi import APIRouter


from pydantic import BaseModel
from uuid import UUID

router = APIRouter()
scaffold_service_instance = Scaffold_Service(

)

class Create_Scaffold_Request(BaseModel):
    job_id: UUID
    status: Optional[str]
    use: Optional[str]
    resource_id: Optional[UUID]


@router.post("/scaffold/create")
def create_scaffold(request:Create_Scaffold_Request):
    scaffold = Scaffold_Service.create_scaffold_request(request.job_id, request.status, request.use, request.resource_id)
    return scaffold


class Read_Scaffold_Request(BaseModel):
    id: UUID

@router.post("/scaffold/read")
def read_scaffold(request:Read_Scaffold_Request):
    scaffold = Scaffold_Service.read_scaffold(request.id)
    return scaffold

class Read_Scaffold_All_Request(BaseModel):
    id: UUID
    job_id: Optional[str]
    resource_id: Optional[str]


@router.post("/scaffold/read_all")
def read_scaffold_all(request):
    scaffold = Scaffold_Service.read_scaffold_all(request.scaffold_id, request.job_id, request.resource_id)
    return scaffold


class Update_scaffold_Request(BaseModel):
    id: UUID
    job_id: UUID
    status: Optional[str]
    use: Optional[str]
    resource_id: Optional[UUID]

@router.post("/scaffold/update")
def update_scaffold(request:Update_scaffold_Request):
    scaffold = Scaffold_Service.read_scaffold_all(request.id, request.job_id, request.status, request.use, request.resource_id)
    return scaffold


class Delete_scaffold_Request(BaseModel):
    id: UUID

@router.post("/scaffold/delete")
def delete_scaffold(request:Delete_scaffold_Request):
    scaffold = Scaffold_Service.delete_scaffold(request.id)
    return scaffold



class Create_Scaffold_Elevation_Request(BaseModel):
    elevation: str
    height:str
    width:str
    chimney:str
    notes: str

@router.post("/scaffold/create_elevation")
def create_scaffold_elevation(request:Create_Scaffold_Elevation_Request):
    scaffold_elevation = Scaffold_Service.create_Scaffold_Elevation_Request(request.elevation, request.height, request.width, request.chimney, request.notes)
    return scaffold_elevation


class Read_Scaffold_Elevation_Request(BaseModel):
    id: UUID

@router.post("/scaffold_elevation/read_elevation")
def read_scaffold_elevation(request:Read_Scaffold_Elevation_Request):
    scaffold_elevation = Scaffold_Service.read_scaffold_elevation(request.id)
    return scaffold_elevation

class Read_scaffold_elevation_All_Request(BaseModel):
    id: UUID
    job_id: Optional[str]
    resource_id: Optional[str]


@router.post("/scaffold_elevation/read_elevation_all")
def read_scaffold_elevation_all(request):
    scaffold_elevation = Scaffold_Service.read_scaffold_elevation_all(request.elevation, request.height, request.width, request.chimney, request.notes)
    return scaffold_elevation


class Update_Scaffold_Elevation_Request(BaseModel):
    id: UUID
    elevation: Optional[str]
    height: Optional[str]
    width: Optional[str]
    chimney: Optional[str]
    notes: Optional[str]

@router.post("/scaffold_elevation/update_elevation")
def update_scaffold_elevation(request:Update_Scaffold_Elevation_Request):
    scaffold_elevation = Scaffold_Service.read_scaffold_elevation_all(request.id, request.elevation, request.height, request.width, request.chimney, request.notes)
    return scaffold_elevation


class Delete_Scaffold_Elevation_Request(BaseModel):
    id: UUID

@router.post("/scaffold_elevation/delete_elevation")
def delete_scaffold_elevation(request:Delete_Scaffold_Elevation_Request):
    scaffold_elevation = Scaffold_Service.delete_scaffold_elevation(request.id)
    return scaffold_elevation



class Create_Scaffold_Checklist_Item_Request(BaseModel):
    check_item: str

@router.post("/scaffold/create_checklist_item")
def create_Scaffold_Checklist_Item(request:Create_Scaffold_Checklist_Item_Request):
    scaffold_checklist_item = Scaffold_Service.create_scaffold_checklist_item_Request(request.check_item)
    return scaffold_checklist_item


class Read_Scaffold_Checklist_Item_Request(BaseModel):
    id: UUID

@router.post("/scaffold/read_checklist_item")
def read_Scaffold_Checklist_Item(request:Read_Scaffold_Checklist_Item_Request):
    scaffold_checklist_item = Scaffold_Service.read_scaffold_checklist_item(request.id)
    return scaffold_checklist_item

class Read_Scaffold_Checklist_Item_All_Request(BaseModel):
    id: UUID
    check_item: str


@router.post("/scaffold/read_checklist_item_all")
def read_Scaffold_Checklist_Item_all(request):
    scaffold_checklist_item = Scaffold_Service.read_scaffold_checklist_item_all(request.check_item)
    return scaffold_checklist_item


class Update_Scaffold_Checklist_Item_Request(BaseModel):
    id: UUID
    check_item: Optional[str]

@router.post("/scaffold_checklist_item/update_checklist_item")
def update_Scaffold_Checklist_Item(request:Update_Scaffold_Checklist_Item_Request):
    scaffold_checklist_item = Scaffold_Service.read_scaffold_checklist_item_all(request.id, request.check_item)
    return scaffold_checklist_item


class Delete_Scaffold_Checklist_Item_Request(BaseModel):
    id: UUID

@router.post("/scaffold_checklist_item/delete_checklist_item")
def delete_Scaffold_Checklist_Item(request:Delete_Scaffold_Checklist_Item_Request):
    scaffold_checklist_item = Scaffold_Service.delete_scaffold_checklist_item(request.id)
    return scaffold_checklist_item



class Create_Scaffold_Media_Request(BaseModel):
    scaffold_id: UUID
    document_name: str
    document: str
    scaffold_checklist_item_id: UUID
    scaffold_media_type: str

@router.post("/scaffold/create_checklist_item")
def create_scaffold_media(request:Create_Scaffold_Media_Request):
    scaffold_checklist_item = Scaffold_Service.create_scaffold_media_request(request.scaffold_id, request.document_name, request.document, request.scaffold_checklist_item_id, request.scaffold_media_type)
    return scaffold_checklist_item


class Read_Scaffold_Media_Request(BaseModel):
    id: UUID

@router.post("/scaffold/read_checklist_item")
def read_scaffold_media(request:Read_Scaffold_Media_Request):
    scaffold_checklist_item = Scaffold_Service.read_scaffold_media(request.id)
    return scaffold_checklist_item

class Read_Scaffold_Media_All_Request(BaseModel):
    scaffold_id: Optional[UUID]
    document_name: Optional[str]
    document: Optional[str]
    scaffold_checklist_item_id: Optional[UUID]
    scaffold_media_type: Optional[str]


@router.post("/scaffold/read_checklist_item_all")
def read_scaffold_media_all(request):
    scaffold_checklist_item = Scaffold_Service.read_Scaffold_Media_all(request.scaffold_id, request.document_name, request.document, request.scaffold_checklist_item_id, request.scaffold_media_type)
    return scaffold_checklist_item


class Update_Scaffold_Media_Request(BaseModel):
    id: UUID
    scaffold_id: Optional[UUID]
    document_name: Optional[str]
    document: Optional[str]
    scaffold_checklist_item_id: Optional[UUID]
    scaffold_media_type: Optional[str]

@router.post("/scaffold_checklist_item/update_checklist_item")
def update_scaffold_media(request:Update_Scaffold_Media_Request):
    scaffold_checklist_item = Scaffold_Service.read_scaffold_media_all(request.id, request.scaffold_id, request.document_name, request.document, request.scaffold_checklist_item_id, request.scaffold_media_type)
    return scaffold_checklist_item


class Delete_Scaffold_Media_Request(BaseModel):
    id: UUID

@router.post("/scaffold_checklist_item/delete_checklist_item")
def delete_scaffold_media(request:Delete_Scaffold_Media_Request):
    scaffold_checklist_item = Scaffold_Service.delete_scaffold_media(request.id)
    return scaffold_checklist_item