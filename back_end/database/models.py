"""
SQLAlchemy models. Each model that holds PII declares ENCRYPTED_FIELDS +
SEARCHABLE_FIELDS and gets an encrypting __init__ per scaffolding-compliance G1.
"""

import datetime as _datetime
import json
import time
import uuid
import enum
from datetime import datetime, timedelta, timezone

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    LargeBinary,
    Numeric,
    String,
    Text,
    and_,
    func,
    Enum,
)
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm import relationship

from back_end.business_objects.Crypto import crypto
from back_end.utils.config import settings

from .database import Base, SessionLocal, get_db_context


class Role(Base):
    __tablename__ = "roles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), unique=True, nullable=False)
    level = Column(Integer, nullable=False)  # Higher = more permissions
    created_timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    users = relationship("User", back_populates="role")

    def __repr__(self):
        return f"<Role {self.name} (level={self.level})>"
    

# >>>>>>>>>> Complaints
    
# Sets the options for each complaint stage as an enum into the database
class ComplaintStage(enum.Enum):
    MEMBER_MP_ENQUIRY = 'Member_MP_Enquiry'
    STAGE_1 = 'Stage 1'
    STAGE_2 = 'Stage 2'
    OMBUDSMAN = 'Ombudsman'

# Creates the py_complaints table. PY added so I can diffrentiate from the tables created in SQL
class PY_Complaints(Base):
    # Sets the table name 
    __tablename__ = "py_complaints"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    complaint_number = Column(String(20), unique=True)

    stage = Column(Enum(ComplaintStage), default = ComplaintStage.MEMBER_MP_ENQUIRY)
    address = Column(String(100))
    postcode = Column(String(10))

# >>>>>>>>>> Jobs
# Created table for jobs to be stored, with a foreign key to the PY Complaints table.
class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    job_number = Column(String(50), unique=True)
    address = Column(String(100))
    postcode = Column(String(10))

    # Foreign key connection to the complaints table
    complaint_id = Column(UUID(as_uuid=True), ForeignKey("py_complaints.id"), nullable=True)

class Job_Stages(Base):
    __tablename__ = "job_stages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(50))
    for_scaffold = Column(Boolean, default=False)

class Job_Stages_History(Base):
    __tablename__ = "job_stages_history"
    id  = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    job_id = Column(UUID(as_uuid=True), ForeignKey("jobs.id"), nullable=False)
    stages_id = Column(UUID(as_uuid=True), ForeignKey("job_stages.id"), nullable=False)
    date = Column(DateTime, default=func.now(), nullable=False)

# >>>>>>>>>> Resources
class resource(Base):
    __tablename__ = "resource"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(60), nullable=False)
    subcontractor = Column(Boolean, default=False)

class resource_contact(Base):
    __tablename__ = "resource_contact"
    id  = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    resource_id = Column(UUID(as_uuid=True), ForeignKey("resource.id"), nullable=False)
    subcontractor = Column(Boolean)
    Name = Column(String(60), nullable=False)
    email = Column(String(100))
    phone = Column(String(15))
    role = Column(String(50))
    
class resource_trade(Base):
    __tablename__ = "resource_trade"

    id  = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    trade = Column(String(50), nullable=False)

# >>>>>>>>>> Scaffold
class scaffold_stage(enum.Enum):
    REQUESTED = 'Requested'
    SENT_TO_COMMERCIAL = 'Sent to commercial'
    SENT_TO_RBK = 'Sent to RBK'
    APPROVED = 'Approved'
    RISK_ASSESSMENTS = 'Risk assessments'
    PERMIT_TO_ERECT = 'Permit to erect'
    HANDOVER_CHECKS = 'Handover checks'
    PERMIT_TO_LOAD = 'Permit to load'
    WORK_COMPLETED = 'Work Completed'
    OFF_HIRE_NOTICE = 'Off-hire notice'
    STRIKE = 'Strike'
    COMPLETED = "Completed"


class Scaffold_Requests(Base):
    __tablename__ = "scaffold_requests"

    id  = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    job_id = Column(UUID(as_uuid=True), ForeignKey("jobs.id"))
    use = Column(String(100))
    status = Column(Enum(scaffold_stage), default=scaffold_stage.REQUESTED)
    resourse_id = Column(UUID(as_uuid=True), ForeignKey("resource.id"))

class scaffold_elevation(enum.Enum):
    FRONT = 'Front'
    LEFT = 'Left'
    RIGHT = 'Right'
    REAR = 'Rear'

class Scaffold_Elevations(Base):
    __tablename__ = "scaffold_elevations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    scaffold_id = Column(UUID(as_uuid=True), ForeignKey("scaffold_requests.id"), nullable=False)
    elevation = Column(Enum(scaffold_elevation), default=scaffold_elevation.FRONT)
    height = Column(Integer)
    width = Column(Integer)
    chimney = Column(Boolean, default=False)
    notes = Column(String(250))    

class Scaffold_Checklist_Item(Base):
    __tablename__ = "scaffold_checklist_item"

    id = Column(UUID(as_uuid=False), primary_key=True, default=uuid.uuid4)
    check_item = Column(String(50))

class Scaffold_Media_Type(enum.Enum):
    REQUEST = 'Request'               
    TG20 = 'TG20'                  
    HANDOVER_CERTIFICATE = 'Handover Certificate'
    SCAFFOLD_TAG = 'Scaffold Tag'          
    SCAFFOLD_PIRCTURE= 'Scaffold Picture'      
    INSPECTION = 'Inspection'            
    OTHER = 'Other' 

class Scaffold_Media(Base):
    __tablename__ = "scaffold_media"

    id  = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    scaffold_id = Column(UUID(as_uuid=True), ForeignKey("scaffold_requests.id"), nullable=False)
    document_name = Column(String(60), nullable=False)
    document = Column(LargeBinary, nullable=False)
    scaffold_checklist_item_id = Column(UUID(as_uuid=True), ForeignKey("scaffold_checklist_item.id"), nullable=False)

"""
python3 -m back_end.scripts.run_migration create -m "Initial Migration"
python3 -m back_end.scripts.run_migration upgrade

"""