# Démarre l'application
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .db import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get a DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/contributions", response_model=schemas.ContributionRead)
def create_contribution(contrib: schemas.ContributionCreate, db: Session = Depends(get_db)):
    db_contrib = models.Contribution(source_id=contrib.source_id, titre=contrib.titre, corps=contrib.corps,
                                  categorie_id=contrib.categorie_id, distance=contrib.distance,
                                  similarite=contrib.similarite)
    db.add(db_contrib)
    db.commit()
    db.refresh(db_contrib)
    return db_contrib