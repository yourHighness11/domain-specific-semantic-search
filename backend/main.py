from fastapi import FastAPI,Form
from fastapi.middleware.cors import CORSMiddleware
from backend.models import TextModel
from backend.embedder import text_embed
from backend.retrieve import query_from_database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

@app.post("/check")
async def check_availablity(req:TextModel):
    print(req.text)
    if(len(req.text) == 0):
        return TextModel(text ="Please enter something..")
    
    embeddings = text_embed(req.text)
    query_result = query_from_database(embeddings,req.top_k)
    print(query_result)
    return {"query_result":query_result.to_dict()}
