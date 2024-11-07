from pydantic import BaseModel
from fastapi import APIRouter, Depends
from ..repositories.architecture_advisor import ArchitectureAdvisor
from ..core.container import Container

router = APIRouter()

class ArchitectureRequest(BaseModel):
    query: str
    nonfunctional_req: str | None = None
    technical_specs: str | None = None

@router.post("/analyze-architecture")
async def analyze_architecture(    
    request: ArchitectureRequest,
    advisor: ArchitectureAdvisor = Depends(lambda: Container().architecture_advisor())
):
    """Analyze requirements and provide architecture recommendations"""
    result = await advisor.analyze_requirements(
        query=request.query,
        nonfunctional_req=request.nonfunctional_req,
        technical_specs=request.technical_specs
    )
    return result 