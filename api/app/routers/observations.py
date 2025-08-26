from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Observation)
def create_observation(obs: schemas.ObservationCreate, db: Session = Depends(get_db), tenant_id: str = Header(..., alias="X-Tenant")):
    db_obs = models.Observation(**obs.dict(), tenant_id=tenant_id)
    db.add(db_obs)
    db.commit()
    db.refresh(db_obs)
    return db_obs

@router.get("/{obs_id}", response_model=schemas.Observation)
def read_observation(obs_id: int, db: Session = Depends(get_db), tenant_id: str = Header(..., alias="X-Tenant")):
    obs = db.query(models.Observation).filter_by(id=obs_id, tenant_id=tenant_id).first()
    if not obs:
        raise HTTPException(status_code=404, detail="Observation not found")
    return obs
