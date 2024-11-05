interface AnalysisResultProps {
  result: string;
}

const AnalysisResult = ({ result }: AnalysisResultProps) => {
  if (!result) return null;

  return (
    <div className="mt-8 w-full p-4 border rounded-lg">
      <h3 className="font-bold mb-2">Analysis Result:</h3>
      <p>{result}</p>
    </div>
  );
};

export default AnalysisResult;
