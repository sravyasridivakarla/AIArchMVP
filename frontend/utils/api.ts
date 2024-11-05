

interface AnalyzeResponse {
  result: string;
}

export const analyzeProduct = async (prompt: string): Promise<AnalyzeResponse> => {
  const response = await fetch('http://localhost:8000/search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query: prompt, limit: 2 }),
  });

  if (!response.ok) {
    throw new Error('Failed to analyze product');
  }


  return {result: await response.json()};
}; 