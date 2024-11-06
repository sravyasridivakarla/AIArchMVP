from pydantic import BaseModel
from fastapi import APIRouter, Depends
from ...src.repositories.vector_repository import VectorRepository
from ...src.core.container import Container

router = APIRouter()

class SearchRequest(BaseModel):
    query: str
    limit: int = 2

@router.post("/search")
async def search(    
    request: SearchRequest,
    vector_repository: VectorRepository = Depends(lambda: Container().vector_repository())
):
    result = vector_repository.search_tech_stack(request.query, request.limit)
    
    if result:
        return {result}
    return {"error": "No results found"}