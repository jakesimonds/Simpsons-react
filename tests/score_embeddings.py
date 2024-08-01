import ollama
import json
from openai import OpenAI
from dotenv import load_dotenv
import os
import chromadb
load_dotenv('../.env')
openAI_key = os.getenv('OPENAI_KEY')
client = OpenAI(api_key=openAI_key)

'''
THINGS TO CHANGE!!!!
'''
#client_ch = chromadb.PersistentClient(path="./db_arctic")
client_ch = chromadb.PersistentClient(path="./db")
collection = client_ch.get_collection(name="docs")

MODEL = 'avr/sfr-embedding-mistral:q4_k_m'
#MODEL = 'snowflake-arctic-embed:latest'
#MODEL = 'mxbai-embed-large:latest'
#MODEL = 'text-embedding-3-large'
#MODEL = 'text-embedding-3-small'
#MODEL = 'nomic-embed-text:latest'
#MODEL = 'all-minilm:latest'

def process_prompt(prompt, collection):
    emb = generate_embedding_local(prompt, MODEL)
    #emb = generate_embedding_openAI(prompt, MODEL)
    results = collection.query(
        query_embeddings=[emb],
        n_results=N_RESULTS
    )
    return [item for sublist in results['documents'] for item in sublist]

'''
THINGS TO CHANGE ^
'''

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


N_RESULTS = 3
INPUT_FILE = "test_queries.txt"
ANSWER_FILE = "test_answers.txt"
OUTPUT_FILE = f"Scores-{MODEL}.json"





# ... (keep all the imports and setup code as is)

results = {}
total_score = 0

with open(INPUT_FILE, 'r') as file1, open(ANSWER_FILE, 'r') as file2:
    prompts = file1.read().splitlines()
    answers = file2.read().splitlines()

if len(prompts) != len(answers):
    raise ValueError("Number of prompts and answers don't match")

# Process each prompt and score
for prompt, answer in zip(prompts, answers):
    query_results = process_prompt(prompt, collection)
    
    score = 0
    for i, result in enumerate(query_results):
        character_name = result.split(':')[0].strip()
        if character_name.lower() == answer.lower():
            score = 3 - i  # 3 points for first, 2 for second, 1 for third
            break
    
    total_score += score
    
    # Store all information in the results dictionary
    results[prompt] = {
        "expected": answer,
        "results": query_results,
        "score": score
    }

# Calculate percentage score
max_possible_score = len(prompts) * 3
percentage_score = (total_score / max_possible_score) * 100

# Add total scores to results
results["summary"] = {
    "total_score": total_score,
    "max_possible_score": max_possible_score,
    "percentage_score": percentage_score
}

# Write results to JSON file
#with open(OUTPUT_FILE, 'w') as file:
with open('k_m.json', 'w') as file:
    json.dump(results, file, indent=2)

print(f"Results have been written to {OUTPUT_FILE}")
print(f"Total Score: {total_score}/{max_possible_score}")
print(f"Percentage Score: {percentage_score:.2f}%")