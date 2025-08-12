import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()
pc = Pinecone(api_key = os.environ.get("PINECONE_API_KEY"), environment = os.environ.get("PINECONE_ENV"))
index_name = "pdf-test"
index = pc.Index(index_name)


def query_from_database(embeddings,top_k = 5):
    print(embeddings,top_k)
    query_vector = embeddings[0].tolist()  # example: use first embedding
    result = index.query(vector=query_vector, top_k=top_k, include_metadata=True)
    return result