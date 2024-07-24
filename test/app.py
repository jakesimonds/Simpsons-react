from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.decomposition import PCA
import ollama

app = FastAPI()

MODEL = 'snowflake-arctic-embed:latest'
strings = ['low', 'cold', 'high', 'hot']

# Initialize PCA and get initial embeddings
vectors = [ollama.embeddings(model=MODEL, prompt=string)['embedding'] for string in strings]
pca = PCA(n_components=2)
vectors_2d = pca.fit_transform(vectors)

class DartInput(BaseModel):
    word: str

@app.post("/get_coordinates")
async def get_coordinates(dart_input: DartInput):
    dart_vec = ollama.embeddings(model=MODEL, prompt=dart_input.word)['embedding']
    dart_2d = pca.transform([dart_vec])[0]
    
    return {
        "fixed_points": [
            {"word": word, "x": float(x), "y": float(y)} 
            for word, (x, y) in zip(strings, vectors_2d)
        ],
        "dart": {"word": dart_input.word, "x": float(dart_2d[0]), "y": float(dart_2d[1])}
    }