from pymilvus import MilvusClient, model

class VectorRepository:
    def __init__(self):
        self.client = MilvusClient("milvus_demo.db")
        self.embedding_fn = model.DefaultEmbeddingFunction()
        self.collection_name = "starter_tech_stack_collection"
        self.initialize()
    
    def initialize(self):
        """Initialize the repository with required setup"""
        self.setup_collection()
        self.insert_initial_data()
    
    def setup_collection(self):
        if self.client.has_collection(collection_name=self.collection_name):
            self.client.drop_collection(collection_name=self.collection_name)
        
        self.client.create_collection(
            collection_name=self.collection_name,
            dimension=768,
        )

    def insert_initial_data(self):
        starter_tech_stack_names = [
            "React", "Vue", "Angular", 
        ]

        docs = [
            "Metrics: High performance, scalable, Compatibility: Compatible with most libraries, Trends: Widely adopted in industry, Use Cases: Web apps, SaaS, Security: Moderate risk of XSS",
            "Metrics: Small size, fast, Compatibility: Highly flexible, Trends: Increasing in popularity, Use Cases: Single-page applications, Security: Moderate risk of XSS",
            "Metrics: Complex but powerful, Compatibility: Works best with TypeScript,Trends: Stable enterprise use, Use Cases: Large-scale apps, Security: Good security with proper setup"
        ]

        vectors = self.embedding_fn.encode_documents(docs)

        data = [
            {"id": i, "vector": vectors[i], "text": docs[i], "name": starter_tech_stack_names[i]}
            for i in range(len(vectors))
        ]

        return self.client.insert(collection_name=self.collection_name, data=data)

    def search_tech_stack(self, query: str, limit: int = 1):
        query_vectors = self.embedding_fn.encode_queries([query])
        
        res = self.client.search(
            collection_name=self.collection_name,
            data=query_vectors,
            limit=limit,
            output_fields=["name"],
        )
        
        try:
            if res[0][0] and res[0][0].get("entity"):
                return res[0][0].get("entity").get("name")
        except Exception as e:
            print(e)
            return None