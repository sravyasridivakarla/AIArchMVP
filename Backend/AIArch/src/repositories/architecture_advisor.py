from ..services.openai_service import OpenAIService
from ..core.constants.arch_constants import GENERIC_NON_FUNCTIONAL_REQUIREMENTS, GENERIC_TECHNICAL_SPECIFICATIONS, ARCHITECTURE_ADVISOR_REQUIREMENTS, TEMPLATE_PROMPT_MARKDOWN, ARCHITECTURE_ADVISOR_ASK

class ArchitectureAdvisor:
    
    def __init__(self, openai_service: OpenAIService):  # Dependency injected
        self.openai_service = openai_service
    
    def _build_system_prompt(self):
        return f"please format the response in markdown format and format it similar to this example markdown with the similar headings: {TEMPLATE_PROMPT_MARKDOWN}"
    def _build_user_prompt(self, query: str,  nonfunctional_req: str = None, technical_specs: str = None):
        return f"This is the business use case: {query} /n {ARCHITECTURE_ADVISOR_ASK} /n Non Functional Requirements: {nonfunctional_req or GENERIC_NON_FUNCTIONAL_REQUIREMENTS} /n Technical Specifications: {technical_specs or GENERIC_TECHNICAL_SPECIFICATIONS} /n {ARCHITECTURE_ADVISOR_REQUIREMENTS}"


    def analyze_requirements(self, query: str, nonfunctional_req: str = None, technical_specs: str = None):
        """Uses the injected service to make the API call"""
        response = self.openai_service.generate_completion(
            system_prompt=self._build_system_prompt(),
            user_query=self._build_user_prompt(query, nonfunctional_req, technical_specs),
        )

        if response["status"] == "success":
            return {
                "status": response["status"],
                "architecture_analysis": response["content"]
            }
        return response
    


