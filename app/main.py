from fastapi import FastAPI

from app.routers.health import router as health_router
from app.routers.semantic_search import router as semantic_search_router
from app.routers.nli import router as nli_router


app = FastAPI(
    title="M5 - API principale consultations citoyennes",
    version="1.0.0",
    description="API d'orchestration des modules M1, M2, M3 et M4/M6.",
)

app.include_router(health_router)
app.include_router(semantic_search_router)
app.include_router(nli_router)


@app.get("/")
def root():
    return {
        "message": "API principale M5",
        "status": "running",
    }