import { useState } from "react";
import LoadingButton from "./DesignComponents/LoadingButton";

interface ProductFormProps {
  onSubmit: (input: string) => Promise<void>;
}

const ProductForm = ({ onSubmit }: ProductFormProps) => {
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const handleSubmit = async () => {
    setIsLoading(true);
    await onSubmit(input);
    setIsLoading(false);
  };

  return (
    <div className="w-full flex flex-col gap-4">
      <h2 className="text-lg text-center">
        Tell me about the product you want to build. Include whatever technical
        details necessary
      </h2>
      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        className="w-full p-4 border rounded-lg min-h-[200px]"
        placeholder="Describe your product..."
      />
      <LoadingButton
        onClick={handleSubmit}
        isLoading={isLoading}
        className="self-center"
      >
        Submit
      </LoadingButton>
    </div>
  );
};

export default ProductForm;
