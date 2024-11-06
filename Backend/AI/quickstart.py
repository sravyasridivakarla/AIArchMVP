from pymilvus import MilvusClient
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymilvus import model


app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/search")
async def root(query: str, limit: int = 2):
    client = MilvusClient("milvus_demo.db")

    if client.has_collection(collection_name="starter_tech_stack_collection"):
        client.drop_collection(collection_name="starter_tech_stack_collection")
    client.create_collection(
        collection_name="starter_tech_stack_collection",
        dimension=768,  # The vectors we will use in this demo has 768 dimensions
    )

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

    data = [
        {"id": i, "vector": vectors[i], "text": docs[i], "name": starter_tech_stack_names[i]}
        for i in range(len(vectors))
    ]


    res = client.insert(collection_name="starter_tech_stack_collection", data=data)



    query_vectors = embedding_fn.encode_queries([query])

    res = client.search(
        collection_name="starter_tech_stack_collection",  # target collection
        data=query_vectors,  # query vectors
        limit=1,  # number of returned entities
        output_fields=["name"],  # specifies fields to be returned
    )
    print(res[0][0].get("entity"))
    try:
        if res[0][0] and res[0][0].get("entity"):
            return {res[0][0].get("entity").get("name")}
    except Exception as e:
        print(e)
        return {"error": "No results found"}




