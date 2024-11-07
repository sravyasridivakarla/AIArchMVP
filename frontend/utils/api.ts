
export const analyzeArchitecture = async (query: string, nonfunctional_req?: string, technical_specs?: string): Promise<string> => {
  const response = await fetch('http://localhost:8000/analyze-architecture', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query , nonfunctional_req, technical_specs}),
  });

  if (!response.ok) {
    throw new Error('Failed to analyze architecture');
  }


  const data = await response.json();


  return data.architecture_analysis
}; 

export const getFramework = async (prompt: string): Promise<string> => {
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

  return response.json()
}; 