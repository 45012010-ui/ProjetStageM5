from typing import List, Optional

import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.config import M2_API_URL


router = APIRouter(tags=["M2 - Recherche sémantique"])


class SemanticSearchRequest(BaseModel):
    query: str = Field(..., min_length=1)
    k: int = Field(default=5, ge=1, le=20)


class SemanticSearchResult(BaseModel):
    id: str
    source_id: Optional[str] = None
    titre: Optional[str] = None
    corps: Optional[str] = None
    categorie: Optional[str] = None
    distance: float
    similarite: float


class SemanticSearchResponse(BaseModel):
    query: str
    k: int
    results: List[SemanticSearchResult]


@router.post(
    "/semantic-search/search",
    response_model=SemanticSearchResponse,
    summary="Recherche sémantique via le module M2",
)
async def semantic_search(request: SemanticSearchRequest):
    """
    Route M5 qui appelle le module M2.

    M5 reçoit la requête utilisateur, appelle M2,
    puis retourne les résultats au même format.
    """
    url = f"{M2_API_URL.rstrip('/')}/semantic-search/search"

    try:
        async with httpx.AsyncClient(timeout=90.0) as client:
            response = await client.post(
                url,
                json=request.model_dump(),
            )

        response.raise_for_status()
        return response.json()

    except httpx.HTTPStatusError as error:
        raise HTTPException(
            status_code=error.response.status_code,
            detail=error.response.text,
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail=f"Impossible de joindre le module M2 à l'adresse {M2_API_URL}",
        )