"use client";
import { useState } from "react";
import Header from "@/components/Header";
import Sidebar from "@/components/Sidebar";
import MainContent from "@/components/MainContent";
import ProductForm from "@/components/ProductForm";

export default function Home() {
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [showForm, setShowForm] = useState(false);

  const handleSubmit = async (input: string) => {
    try {
      console.log(input);
      setIsSubmitted(true);
      setShowForm(false); // Hide form after submission
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const handleCreateClick = () => {
    setShowForm(true);
    setIsSubmitted(false);
  };

  return (
    <div className="min-h-screen flex flex-col">
      <Header onCreateClick={handleCreateClick} />
      {showForm ? (
        // Form view
        <div className="flex-1 container mx-auto py-8">
          <ProductForm onSubmit={handleSubmit} />
        </div>
      ) : isSubmitted ? (
        // Architecture view
        <div className="flex flex-1">
          <Sidebar />
          <MainContent />
        </div>
      ) : (
        // Initial/empty state
        <div className="flex-1 flex items-center justify-center">
          <p className="text-gray-500">Click Create to start a new project</p>
        </div>
      )}
    </div>
  );
}
