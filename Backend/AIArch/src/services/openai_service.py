from openai import OpenAI
from typing import Dict, Any
from ..core.gpt_constants import GPT_MODEL, TEMPERATURE, MAX_TOKENS

class OpenAIService:
    def __init__(self, client: OpenAI):
        self.client = client

    def generate_completion(
        self,
        system_prompt: str,
        user_query: str,
        model: str = GPT_MODEL,
        temperature: float = TEMPERATURE,
        max_tokens: int = MAX_TOKENS
    ) -> Dict[str, Any]:
        """Handles the API call to OpenAI"""
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_query}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            if response.choices and response.choices[0].message:
                return {
                    "status": "success",
                    "content": response.choices[0].message.content
                }
            
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error generating completion: {str(e)}"
            } 