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

def return_index(string):


    def create_line_dictionary(file_path):
        line_dict = {}
        
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):
                line_dict[line_number] = line.strip()
        
        return line_dict

    # Example usage
    file_path = 'simpsons_opt.txt'  # Replace with your file path
    result = create_line_dictionary(file_path)

    # Print the resulting dictionary
    for key, value in result.items():
        if string in value:
            return key
    return 1

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
    return {"message": "Hello World"}

@app.post("/query")
async def query(request: Request):
    data = await request.json()
    PROMPT = data['text']

    chroma_client = chromadb.PersistentClient(path="./db")
    collection = chroma_client.get_collection(name="docs")
    print("TEST TEST")


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
    data = results['documents'][0]
    
    #print(data)
    
    to_return = []
    
    for string in data:
        to_return.append({return_index(string): string}) 
    print(to_return)
    



    flat_list = [item for sublist in data for item in sublist]
    #print(data)
    return {"result": to_return}


if __name__ == "__main__":
    import uvicorn
    #uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn.run(app, host="0.0.0.0", port=8000)



