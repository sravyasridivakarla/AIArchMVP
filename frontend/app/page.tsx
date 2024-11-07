"use client";
import { useState } from "react";
import Header from "../components/Header";
import ProductForm from "../components/ProductForm";
import AnalysisResult from "../components/AnalysisResult";
import { analyzeArchitecture } from "../utils/api";

export default function Home() {
  const [result, setResult] = useState<string>("");

  const handleSubmit = async (input: string) => {
    try {
      const response = await analyzeArchitecture(input);
      setResult(response);
    } catch (error) {
      console.error("Error:", error);
      // You might want to add error handling UI here
      setResult("error fetching result: " + error);
    }
  };

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-1 flex flex-col items-center justify-center p-4 max-w-2xl mx-auto">
        <ProductForm onSubmit={handleSubmit} />
        <AnalysisResult result={result || ""} />
      </main>
    </div>
  );
}
