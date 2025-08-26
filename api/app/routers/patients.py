from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db), tenant_id: str = Header(..., alias="X-Tenant")):
    db_patient = models.Patient(**patient.dict(), tenant_id=tenant_id)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.get("/{patient_id}", response_model=schemas.Patient)
def read_patient(patient_id: int, db: Session = Depends(get_db), tenant_id: str = Header(..., alias="X-Tenant")):
    patient = db.query(models.Patient).filter_by(id=patient_id, tenant_id=tenant_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.get("/", response_model=list[schemas.Patient])
def list_patients(db: Session = Depends(get_db), tenant_id: str = Header(..., alias="X-Tenant")):
    return db.query(models.Patient).filter_by(tenant_id=tenant_id).all()

@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db), tenant_id: str = Header(..., alias="X-Tenant")):
    patient = db.query(models.Patient).filter_by(id=patient_id, tenant_id=tenant_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    db.delete(patient)
    db.commit()
    return {"ok": True}
