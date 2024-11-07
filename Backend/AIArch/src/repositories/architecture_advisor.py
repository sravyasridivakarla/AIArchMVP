from ..services.openai_service import OpenAIService

class ArchitectureAdvisor:
    
    def __init__(self, openai_service: OpenAIService):  # Dependency injected
        self.openai_service = openai_service
    
    def _build_system_prompt(self, query: str, nonfunctional_req: str = None, technical_specs: str = None):
        return f"This is the business use case: {query} /n {ARCHITECTURE_ADVISOR_ASK} /n Non Functional Requirements: {nonfunctional_req or GENERIC_NON_FUNCTIONAL_REQUIREMENTS} /n Technical Specifications: {technical_specs or GENERIC_TECHNICAL_SPECIFICATIONS} /n {ARCHITECTURE_ADVISOR_REQUIREMENTS}"
    
    def analyze_requirements(self, query: str, nonfunctional_req: str = None, technical_specs: str = None):
        """Uses the injected service to make the API call"""
        response = self.openai_service.generate_completion(
            system_prompt=self._build_system_prompt(query, nonfunctional_req, technical_specs),
            user_query=query
        )

        if response["status"] == "success":
            return {
                "status": response["status"],
                "architecture_analysis": response["content"]
            }
        return response
    


# System prompts
ARCHITECTURE_ADVISOR_ASK = """You are an expert software architect. Analyze the requirements and provide detailed 
architecture recommendations for the following business use case:"""

ARCHITECTURE_ADVISOR_REQUIREMENTS = """
Provide technical details in each layer.
Provide details of all components involved
Create technical and deployment, security related details. 
Also based on the data, pl. calculate the operational costs
"""

GENERIC_NON_FUNCTIONAL_REQUIREMENTS = """
Total number of monthly active users: 1 billion.
Number of videos watched per day: 4 billion.
50 million users create 
MemoriesAI is available in 80 different languages.
Upload videos should show progress bar
The Search results should return in 800 ms for 50 percentile of users and 1500 ms for 90 percentile of users
Average size of the video is about 500 mb
99.95% Availability
99.999 Reliability
"""
GENERIC_TECHNICAL_SPECIFICATIONS = """
System will use Layered Architecture
Use Microservices architecture
Technology Stack used is React, Python, MySQL, Blog Storage
Use of AWS Cloud based technologies
System should use CDN for video and content distribution
Suggest use of the right Search architecture
"""
