from typing import Literal

import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.config import M3_API_URL


router = APIRouter(tags=["M3 - NLI"])


class NliAnalyzeRequest(BaseModel):
    proposal_a_id: str
    proposal_b_id: str


class NliAnalyzeResponse(BaseModel):
    proposal_a_id: str
    proposal_b_id: str
    relation: str
    score: float
    similarity_m2: float
    model: str
    latency_ms: int


@router.post(
    "/nli/analyze",
    response_model=NliAnalyzeResponse,
    summary="Analyse NLI via le module M3",
)
async def analyze_nli(request: NliAnalyzeRequest):
    """
    Route M5 qui appelle le module M3.

    M5 reçoit deux IDs de propositions,
    appelle M3, puis retourne la relation NLI.
    """
    url = f"{M3_API_URL.rstrip('/')}/api/v1/nli/analyze"

    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
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
            detail=f"Impossible de joindre le module M3 à l'adresse {M3_API_URL}",
        )