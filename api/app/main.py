from fastapi import FastAPI, Depends
from .database import Base, engine
from .routers import patients, observations

app = FastAPI(title="Geriatric B2B API")

# Create tables if not using migrations
Base.metadata.create_all(bind=engine)

app.include_router(patients.router, prefix="/patients", tags=["patients"])
app.include_router(observations.router, prefix="/observations", tags=["observations"])

