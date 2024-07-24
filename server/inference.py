import ollama
import chromadb
import sys
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv('../.env')
OPENAI_KEY = os.getenv('OPENAI_KEY')
client = OpenAI(api_key=OPENAI_KEY)

N_RESULTS = 3
#PROMPT = "bully who says 'Ha-ha!'"
if len(sys.argv) < 2:
  PROMPT = "incompetent worker"
else:
    PROMPT = sys.argv[1]

chroma_client = chromadb.PersistentClient(path="./db")
collection = chroma_client.get_collection(name="docs")


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

# Print each item on a new line
for item in flat_list:
    print(item)
    
    
# evil genius
# tom cruise
# the godfather
# STEM professional
