from datetime import datetime
from pydantic import BaseModel

class PatientBase(BaseModel):
    first_name: str
    last_name: str
    consent: bool = True

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    tenant_id: str

    class Config:
        orm_mode = True

class ObservationBase(BaseModel):
    patient_id: int
    code: str
    value: str | None = None
    timestamp: datetime | None = None

class ObservationCreate(ObservationBase):
    pass

class Observation(ObservationBase):
    id: int
    tenant_id: str

    class Config:
        orm_mode = True
