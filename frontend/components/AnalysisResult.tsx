import ReactMarkdown from "react-markdown";

const AnalysisResult = (props: { result: string }) => {
  const { result } = props;
  if (!result) return null;

  return (
    <div className="mt-8 w-full p-4 border rounded-lg">
      <h3 className="font-bold mb-2">Analysis Result:</h3>
      <ReactMarkdown>{result}</ReactMarkdown>
    </div>
  );
};

export default AnalysisResult;
