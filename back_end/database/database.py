"""
Database session + ModelBase pattern.

ModelBase provides automatic encryption/decryption of fields declared in
ENCRYPTED_FIELDS (via crypto + pii_key_id). All models in this app inherit
from Base, which combines ModelBase with SQLAlchemy's DeclarativeBase.
"""

import base64
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from back_end.business_objects.Crypto import crypto
from back_end.utils.config import settings


class ModelBase:
    """Base mixin with PII-aware get_dict / update_from_dictionary."""

    ENCRYPTED_FIELDS = set()      # PII fields requiring encryption
    SEARCHABLE_FIELDS = set()     # subset using deterministic encryption
    BINARY_FIELDS = set()         # raw bytes (base64-wrapped at the API boundary)
    EXCLUDED_FIELDS = set()       # excluded from get_dict() outputs

    def get_dict(self, db=None):
        result = {}
        for column in self.__table__.columns:
            if column.name in self.EXCLUDED_FIELDS:
                continue

            value = getattr(self, column.name)

            if column.name in self.ENCRYPTED_FIELDS and value:
                value = crypto.decrypt(self.pii_key_id, value)

            if column.name in self.BINARY_FIELDS and value:
                value = base64.b64encode(value).decode("utf-8")

            result[column.name] = value
        return result

    def update_from_dictionary(self, data: dict):
        for key, value in data.items():
            if not hasattr(self, key):
                continue

            if key in self.ENCRYPTED_FIELDS and value:
                is_searchable = key in self.SEARCHABLE_FIELDS
                value = crypto.encrypt(
                    crypto.get_latest_key_id(),
                    value,
                    searchable=is_searchable,
                    data_type=key,
                )
                # Rotation key write -- record the new key id on this row
                self.pii_key_id = crypto.get_latest_key_id()

            if key in self.BINARY_FIELDS and value and isinstance(value, str):
                value = base64.b64decode(value)

            setattr(self, key, value)


class Base(ModelBase, DeclarativeBase):
    """Combined base for every model in this project."""
    pass


engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """FastAPI dependency."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def get_db_context():
    """Context-manager flavour for use outside FastAPI routes."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
