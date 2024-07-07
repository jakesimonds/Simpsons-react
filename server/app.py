
import chromadb
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import ollama  # Ensure you have the correct import for your model

import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / '.env'  # Adjust the path as necessary
load_dotenv(dotenv_path=env_path)




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
async def test(request: Request):
    print("Hit /test in fastAPI Simpsons-retrieval server")
    return {"message": "Hello World"}

@app.post("/query")
async def query(request: Request):
    print("HIT /query in fastAPI Simpsons-retrieval server")
    data = await request.json()
    print(data)
    PROMPT = data['text']
    #PROMPT = 'STEM professional'

    print(PROMPT)

    client = chromadb.PersistentClient(path="./db")
    collection = client.get_collection(name="docs")


    MODEL = 'snowflake-arctic-embed:latest'
    N_RESULTS = 3
    response = ollama.embeddings(
    prompt=PROMPT,
    model=MODEL
    )
    results = collection.query(
    query_embeddings=[response["embedding"]],
    n_results=N_RESULTS
    )
    data = results['documents']


    flat_list = [item for sublist in data for item in sublist]
    #print(data)
    return {"result": data}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



