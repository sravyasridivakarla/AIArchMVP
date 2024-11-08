interface ProposalCardProps {
  number: number;
  selected?: boolean;
}

const ProposalCard = ({ number, selected }: ProposalCardProps) => {
  return (
    <div
      className={`p-4 border rounded-lg mb-4 ${
        selected ? "border-blue-500" : "border-gray-200"
      }`}
    >
      <h3 className="font-medium mb-2">Proposal {number}</h3>
      <div className="grid grid-cols-4 gap-2">
        {[1, 2, 3, 4].map((_, i) => (
          <div key={i} className="h-2 bg-green-500 rounded" />
        ))}
      </div>
    </div>
  );
};

const Sidebar = () => {
  return (
    <div className="w-64 border-r p-4 h-[calc(100vh-64px)]">
      <div className="mb-6">
        <h2 className="font-medium mb-2">Memories AI</h2>
        <p className="text-sm text-gray-600">
          Use case, Architecture Recommendations Tradeoff Analysis
        </p>
      </div>

      {[1, 2, 3, 4].map((num) => (
        <ProposalCard key={num} number={num} selected={num === 1} />
      ))}
    </div>
  );
};

export default Sidebar;
