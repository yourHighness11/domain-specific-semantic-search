from pydantic import BaseModel

class TextModel(BaseModel):
    text:str
    top_k:int