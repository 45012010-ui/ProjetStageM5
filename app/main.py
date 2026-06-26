# Démarre l'application
from fastapi import FastAPI, Depends
from .src import search_api
from sqlalchemy.orm import Session
from . import models
from .db import engine, SessionLocal

#Imports pour fastapi-health
import asyncio
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_health import health

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


# @app.get("/health")
# def health(): #Il faut que ceci vérifie si l'API fonctionne correctement (Est-ce qu'il y a une extension qui permet de faire ça?)
#     return{
#         "status": "ok",
#         "module": "M5 API orchestration"
#     }
#J'ai trouvé une extension appelée fastapi-health qui permet de faire ça, le code en dessous utilise cette extension

def get_session():
    return True
async def is_database_online(session: AsyncSession = Depends(get_session)):
    try:    
        await asyncio.wait_for(session.execute("SELECT 1"), timeout=30)
    except (SQLAlchemyError, TimeoutError): 
        return False
    return True

app.add_api_route("/health", health([is_database_online]))

#Fin du code utilisant fastapi_health

# @app.post("/semantic-search/search")
# def semantic_search(): #Intégrer à partir de M2 
#     return{
#         "place":"holder"
#     }
#Pas nécessaire, inclure le router de search_api devrait déjà permettre d'accéder à semantic_search

@app.post("/nli/analyze")
def nli_analyze(): #Intégrer à partir de M3
    return{
        "place":"holder"
    }
