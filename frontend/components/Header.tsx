import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

interface HeaderProps {
  onCreateClick?: () => void;
}

const Header = ({ onCreateClick }: HeaderProps) => {
  return (
    <div className="w-full bg-blue-950 p-4 flex items-center gap-4">
      <h1 className="text-2xl font-bold text-white">AIARCH</h1>
      <Button variant="secondary" onClick={onCreateClick}>
        Create
      </Button>
      <Button variant="ghost" className="text-white">
        Documents
      </Button>
      <div className="flex-1 max-w-2xl ml-4">
        <Input
          type="search"
          placeholder="Search..."
          className="w-full bg-white/10 text-white"
        />
      </div>
    </div>
  );
};

export default Header;
