#uvicorn app:app --host 0.0.0.0 --port 8000
# uvicorn app:app

import chromadb
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

import os
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI

#env_path = Path(__file__).resolve().parent.parent / '.env'  # Adjust the path as necessary
#load_dotenv(dotenv_path=env_path)
import os

# Initialize the OpenAI client

load_dotenv('../.env')
OPENAI_KEY = os.getenv('OPENAI_KEY')

client = OpenAI(api_key=OPENAI_KEY)





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

    chroma_client = chromadb.PersistentClient(path="./db")
    collection = chroma_client.get_collection(name="docs")


    MODEL = 'snowflake-arctic-embed:latest'
    N_RESULTS = 3
    response = client.embeddings.create(
        input=PROMPT,
        model="text-embedding-3-large"
    )
    prompt_embedding = response.data[0].embedding
    results = collection.query(
    query_embeddings=[prompt_embedding],
    n_results=N_RESULTS
    )
    data = results['documents']


    flat_list = [item for sublist in data for item in sublist]
    #print(data)
    return {"result": data}


if __name__ == "__main__":
    import uvicorn
    #uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn.run(app, host="0.0.0.0", port=8000)



