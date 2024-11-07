from fastapi import APIRouter, Depends
from ..repositories.architecture_advisor import ArchitectureAdvisor
from ..core.container import Container
from pydantic import BaseModel
router = APIRouter()

class ArchitectureRequest(BaseModel):
    query: str

@router.post("/analyze-architecture")
async def analyze_architecture(    
    request: ArchitectureRequest,
    advisor: ArchitectureAdvisor = Depends(lambda: Container().architecture_advisor())
):
    """Analyze requirements and provide architecture recommendations"""
    result = advisor.analyze_requirements(request.query)
    return result