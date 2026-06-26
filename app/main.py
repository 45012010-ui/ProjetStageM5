# Démarre l'application
from fastapi import FastAPI, Depends
from .src import search_api
from sqlalchemy.orm import Session
from . import models
from .db import engine, SessionLocal

#models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API principale - Project consultations citoyennes")
app.include_router(search_api.router)

# Dependency to get a DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Page par défaut"}


@app.get("/health")
def health(): #Il faut que ceci vérifie si l'API fonctionne correctement (Est-ce qu'il y a une extension qui permet de faire ça?)
    return{
        "status": "ok",
        "module": "M5 API orchestration"
    }

@app.post("/semantic-search/search")
def semantic_search(): #Intégrer à partir de M2 
    return{
        "place":"holder"
    }

@app.post("/nli/analyze")
def nli_analyze(): #Intégrer à partir de M3
    return{
        "place":"holder"
    }
