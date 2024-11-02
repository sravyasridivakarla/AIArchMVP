from pymilvus import MilvusClient

client = MilvusClient("milvus_demo.db")

if client.has_collection(collection_name="starter_tech_stack_collection"):
    client.drop_collection(collection_name="starter_tech_stack_collection")
client.create_collection(
    collection_name="starter_tech_stack_collection",
    dimension=768,  # The vectors we will use in this demo has 768 dimensions
)

from pymilvus import model


embedding_fn = model.DefaultEmbeddingFunction()


tech_stach_names = [
    "React", "Vue", "Angular", "Svelte", "Next.js", "Ember", "Backbone", "Polymer", "Meteor", "Knockout", "Dojo", "Mithril", "Marionette", "Aurelia"
]


starter_tech_stack_names = [
    "React", "Vue", "Angular", 
]


docs = [
    "Metrics: High performance, scalable, Compatibility: Compatible with most libraries, Trends: Widely adopted in industry, Use Cases: Web apps, SaaS, Security: Moderate risk of XSS",
    "Metrics: Small size, fast, Compatibility: Highly flexible, Trends: Increasing in popularity, Use Cases: Single-page applications, Security: Moderate risk of XSS",
    "Metrics: Complex but powerful, Compatibility: Works best with TypeScript,Trends: Stable enterprise use, Use Cases: Large-scale apps, Security: Good security with proper setup"
]

vectors = embedding_fn.encode_documents(docs)
print("Dim:", embedding_fn.dim, vectors[0].shape)  # Dim: 768 (768,)

data = [
    {"id": i, "vector": vectors[i], "text": docs[i], "name": starter_tech_stack_names[i]}
    for i in range(len(vectors))
]

print("Data has", len(data), "entities, each with fields: ", data[0].keys())
print("Vector dim:", len(data[0]["vector"]))
res = client.insert(collection_name="starter_tech_stack_collection", data=data)

print(res)

query_vectors = embedding_fn.encode_queries(["Which framework has the best security and can be used for large-scale apps?"])

res = client.search(
    collection_name="starter_tech_stack_collection",  # target collection
    data=query_vectors,  # query vectors
    limit=2,  # number of returned entities
    output_fields=["name"],  # specifies fields to be returned
)

print(res)




