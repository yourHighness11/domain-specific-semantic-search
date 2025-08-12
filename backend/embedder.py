import numpy as np
from InstructorEmbedding import INSTRUCTOR


# --Create embeddings with Instructor-XL --
def text_embed(text:str):
    model = INSTRUCTOR("hkunlp/instructor-xl")
    instruction = "Represent the sentence for semantic search"

    pairs = [[instruction, text]]
    embs = model.encode(pairs, normalize_embeddings=True)  # cosine-friendly
    embs = np.asarray(embs, dtype="float32")
    # dim = embs.shape[1]

    return embs