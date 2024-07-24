


import chromadb
import re
from openai import OpenAI
from dotenv import load_dotenv
import os

# Initialize the OpenAI client

load_dotenv('../.env')
openAI_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=openAI_key)

file_path = './simpsons_opt.txt'

def simpsons_chunks_opt(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    chunks = content.split('\n')
    return chunks

def embed(chunks, collection):
    for i, d in enumerate(chunks):
        response = client.embeddings.create(
            input=d,
            model="text-embedding-3-large"
        )
        embedding = response.data[0].embedding
        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[d]
        )

chroma_client = chromadb.PersistentClient(path="./db")
collection = chroma_client.create_collection(name="docs")

chunks = simpsons_chunks_opt(file_path)

print(f"length of chunks: {len(chunks)}")
print(f"first chunk: {chunks[0]}")

embed(chunks, collection)

prompt = "showbusiness professional"
N_RESULTS = 3

response = client.embeddings.create(
    input=prompt,
    model="text-embedding-3-large"
)
prompt_embedding = response.data[0].embedding

# You can now use this embedding to query your Chroma collection
results = collection.query(
    query_embeddings=[prompt_embedding],
    n_results=N_RESULTS
)

print(results)