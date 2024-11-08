import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { PencilIcon } from "lucide-react";

const SummaryCard = ({
  title,
  content,
  editable = true,
}: {
  title: string;
  content: string;
  editable?: boolean;
}) => {
  return (
    <Card className="mb-6">
      <CardHeader className="flex flex-row items-center justify-between">
        <CardTitle>{title}</CardTitle>
        {editable && (
          <Button variant="ghost" size="icon">
            <PencilIcon className="h-4 w-4" />
          </Button>
        )}
      </CardHeader>
      <CardContent>
        <p className="text-gray-600">{content}</p>
      </CardContent>
    </Card>
  );
};

const ArchitectureSection = ({
  title,
  content,
}: {
  title: string;
  content?: string;
}) => {
  return (
    <div className="h-[500px] w-full bg-gray-50 rounded-lg p-4">
      {content || `${title} content will go here`}
    </div>
  );
};

const MainContent = () => {
  return (
    <div className="flex-1 p-6">
      <div className="grid grid-cols-2 gap-6 mb-6">
        <SummaryCard
          title="Use Case Summary"
          content="MemoriesAI enables users to celebrate video memories, with features like emotion-based organization and sharing..."
        />
        <SummaryCard
          title="Technical Specification Summary"
          content="MemoriesAI aims for massive scalability and resilience with 1 billion monthly users..."
        />
      </div>

      <Tabs defaultValue="technical" className="w-full">
        <TabsList className="grid w-full grid-cols-4">
          <TabsTrigger value="technical">Technical Architecture</TabsTrigger>
          <TabsTrigger value="security">Security Architecture</TabsTrigger>
          <TabsTrigger value="operational">
            Operational Architecture
          </TabsTrigger>
          <TabsTrigger value="cto">CTO Report</TabsTrigger>
        </TabsList>
        <TabsContent value="technical">
          <ArchitectureSection title="Technical Architecture" />
        </TabsContent>
        <TabsContent value="security">
          <ArchitectureSection title="Security Architecture" />
        </TabsContent>
        <TabsContent value="operational">
          <ArchitectureSection title="Operational Architecture" />
        </TabsContent>
        <TabsContent value="cto">
          <ArchitectureSection title="CTO Report" />
        </TabsContent>
      </Tabs>
    </div>
  );
};

export default MainContent;
