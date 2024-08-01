# https://blog.bawolf.com/p/embeddings-are-a-good-starting-point
# https://github.com/chroma-core/chroma

import ollama
import chromadb
import re
from openai import OpenAI
from dotenv import load_dotenv
import os
import json


load_dotenv('../.env')
openAI_key = os.getenv('OPENAI_KEY')

client = OpenAI(api_key=openAI_key)

'''
CHANGE THIS
'''
MODEL = 'avr/sfr-embedding-mistral:q4_k_m'
#MODEL = 'all-minilm:latest'
#MODEL = 'nomic-embed-text:latest'
#MODEL = 'snowflake-arctic-embed:latest'
#MODEL = 'mxbai-embed-large:latest'
#MODEL = 'text-embedding-3-large'
#MODEL = 'text-embedding-3-small'

def embed(MODEL, chunks, collection):
    for i, d in enumerate(chunks):
        embedding = generate_embedding_local(d, MODEL)
        #embedding = generate_embedding_openAI(d, MODEL)
        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[d]
        )
        
def process_prompt(prompt, collection):
    emb = generate_embedding_local(prompt, MODEL)
    #emb = generate_embedding_openAI(prompt, MODEL)
    results = collection.query(
        query_embeddings=[emb],
        n_results=N_RESULTS
    )
    return [item for sublist in results['documents'] for item in sublist]
        
client_ch = chromadb.PersistentClient(path="./db")
collection = client_ch.create_collection(name="docs")
#collection = client_ch.get_collection(name="docs")
'''
CHANGE THIS ^
'''


file_path = './character_strings.txt'


#1024
def generate_embedding_local(string, model):
    response = ollama.embeddings(model=model, prompt=string)
    return response['embedding']

# longer than 1024
def generate_embedding_openAI(string, model):
    response = client.embeddings.create(
    input=string,
    model=model)
    embedding = response.data[0].embedding
    return embedding
    

def chunk_file(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        content = file.read()
    #print(content)
    chunks = content.split('\n')
    return chunks





chunks = chunk_file(file_path)

# print(f"length of chunks: {len(chunks)}")
# print(f"first chunk: {chunks[0]}")


embed(MODEL, chunks, collection)



N_RESULTS = 3
INPUT_FILE = "sample_queries.txt"
OUTPUT_FILE = f"results/test-queries-{MODEL}.json"




results = {}

# Read prompts from file
with open(INPUT_FILE, 'r') as file:
    prompts = file.read().splitlines()

# Process each prompt
for prompt in prompts:
    results[prompt] = process_prompt(prompt, collection)

# Write results to JSON file
with open('k_m.json', 'w') as file:
#with open(OUTPUT_FILE, 'w') as file:
    json.dump(results, file, indent=2)

print(f"Results have been written to {OUTPUT_FILE}")