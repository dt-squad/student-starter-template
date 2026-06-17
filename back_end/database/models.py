"""
SQLAlchemy models. Each model that holds PII declares ENCRYPTED_FIELDS +
SEARCHABLE_FIELDS and gets an encrypting __init__ per scaffolding-compliance G1.
"""

import datetime as _datetime
import json
import time
import uuid
from datetime import datetime, timedelta, timezone

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    and_,
    func,
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

    users = relationship("User", back_populates="role")

    def __repr__(self):
        return f"<Role {self.name} (level={self.level})>"