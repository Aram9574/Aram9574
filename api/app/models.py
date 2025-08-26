from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from .database import Base

class TenantMixin:
    tenant_id = Column(String, index=True)

class Patient(Base, TenantMixin):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    consent = Column(Boolean, default=True)

class Observation(Base, TenantMixin):
    __tablename__ = "observations"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    code = Column(String, nullable=False)
    value = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    patient = relationship("Patient")

class Encounter(Base, TenantMixin):
    __tablename__ = "encounters"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    note = Column(Text)
    start = Column(DateTime, default=datetime.utcnow)
    patient = relationship("Patient")

class Medication(Base, TenantMixin):
    __tablename__ = "medications"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    name = Column(String)
    dosage = Column(String)
    patient = relationship("Patient")

class Appointment(Base, TenantMixin):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    scheduled = Column(DateTime)
    reason = Column(String)
    patient = relationship("Patient")

class CarePlan(Base, TenantMixin):
    __tablename__ = "care_plans"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    description = Column(Text)
    patient = relationship("Patient")

class AuditLog(Base, TenantMixin):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True)
    action = Column(String)
    entity = Column(String)
    entity_id = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(String)
