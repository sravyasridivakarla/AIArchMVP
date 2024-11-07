from openai import OpenAI
from ..repositories.architecture_advisor import ArchitectureAdvisor
from ..services.openai_service import OpenAIService
from .config import get_settings

class Container:
    _architecture_advisor = None
    _openai_client = None
    _openai_service = None

    def openai_client(self) -> OpenAI:
        if not self._openai_client:
            settings = get_settings()
            self._openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)
        return self._openai_client

    def openai_service(self) -> OpenAIService:
        if not self._openai_service:
            self._openai_service = OpenAIService(self.openai_client())
        return self._openai_service

    def architecture_advisor(self) -> ArchitectureAdvisor:
        if not self._architecture_advisor:
            self._architecture_advisor = ArchitectureAdvisor(self.openai_service())
        return self._architecture_advisor 