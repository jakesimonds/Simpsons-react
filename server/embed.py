# https://blog.bawolf.com/p/embeddings-are-a-good-starting-point
# https://github.com/chroma-core/chroma

import ollama
import chromadb
import re
from openai import OpenAI
from dotenv import load_dotenv
import os

# Initialize the OpenAI client

load_dotenv('../.env')
openAI_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=openAI_key)

MODEL = 'snowflake-arctic-embed:latest'
file_path = './simpsons_opt.txt'


#1024
def generate_embedding_local(string, model):
    response = ollama.embeddings(model=model, prompt=string)
    return response['embedding']

# longer than 1024
def generate_embedding_openAI(string):
    response = client.embeddings.create(
    input=string,
    model="text-embedding-3-large")
    embedding = response.data[0].embedding
    return embedding
    

def chunk_file(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        content = file.read()
    #print(content)
    chunks = content.split('\n')
    return chunks

def embed(MODEL, chunks, collection):
    for i, d in enumerate(chunks):
        embedding = generate_embedding_local(d, MODEL)
        #embedding = generate_embedding_openAI(d)
        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[d]
        )




client = chromadb.PersistentClient(path="./db")
collection = client.create_collection(name="docs")


chunks = chunk_file(file_path)

# print(f"length of chunks: {len(chunks)}")
# print(f"first chunk: {chunks[0]}")
embed(MODEL, chunks, collection)
    




prompt = "evil genius"
N_RESULTS = 3

response = ollama.embeddings(
  prompt=prompt,
  model=MODEL
)
results = collection.query(
  query_embeddings=[response["embedding"]],
  n_results=N_RESULTS
)
data = results['documents']

#print(data)

flat_list = [item for sublist in data for item in sublist]

# Print each item on a new line
for item in flat_list:
    print(item)