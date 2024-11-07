TEMPLATE_PROMPT_MARKDOWN = """

## **Architecture Specification for MemoriesAI**\n
\n
### **1. Overview**\n
\n
MemoriesAI enables users to upload, share, classify, and retrieve videos based on memories, emotions, and occasions. This specification outlines the technical, deployment, and security architecture, using AWS Cloud services to ensure scalability, reliability, and performance, meeting non-functional requirements (NFRs) such as 99.95% availability and low-latency search results.\n
\n
### **2. Core Functional Architecture**\n
\n
MemoriesAI will use a **Layered Architecture**, with clear separation of concerns, including the following layers:\n
\n
1. **Presentation Layer:**\n
    * **React** for the front-end to provide a responsive user interface and enable video uploads, video playback, and search.\n
    * Progressive upload with real-time progress bars for video uploads.\n
2. **Application Layer:**\n
    * **Python-based microservices** for handling different business logic components like video upload, speech-to-text conversion, video classification, and search functionality.\n
    * Integration with AWS services for processing and optimizing videos.\n
"""  # ... rest of the template

# System prompts
ARCHITECTURE_ADVISOR_ASK = """You are an expert software architect. Analyze the requirements and provide detailed \n
architecture recommendations for the following business use case:\n"""

ARCHITECTURE_ADVISOR_REQUIREMENTS = """
Provide technical details in each layer.\n
Provide details of all components involved\n
Create technical and deployment, security related details.\n 
Also based on the data, pl. calculate the operational costs\n
"""

GENERIC_NON_FUNCTIONAL_REQUIREMENTS = """
Total number of monthly active users: 1 billion.\n
Number of videos watched per day: 4 billion.\n
50 million users create\n 
MemoriesAI is available in 80 different languages.\n
Upload videos should show progress bar\n
The Search results should return in 800 ms for 50 percentile of users and 1500 ms for 90 percentile of users\n
Average size of the video is about 500 mb\n
99.95% Availability\n
99.999 Reliability\n
"""

GENERIC_TECHNICAL_SPECIFICATIONS = """
System will use Layered Architecture\n
Use Microservices architecture\n
Technology Stack used is React, Python, MySQL, Blog Storage\n
Use of AWS Cloud based technologies\n
System should use CDN for video and content distribution\n
Suggest use of the right Search architecture\n
"""

