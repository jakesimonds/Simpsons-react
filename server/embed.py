# https://blog.bawolf.com/p/embeddings-are-a-good-starting-point
# https://github.com/chroma-core/chroma

import ollama
import chromadb
import re

MODEL = 'snowflake-arctic-embed:latest'
file_path = './simpsons_opt.txt'


# Create chunks from the text with specified chunk size and overlap
def generic_create_chunks(file_path, chunk_size, overlap_size):
    with open(file_path, 'r') as file:
        text = file.read()
    chunks = []
    length = len(text)
    
    for i in range(0, length, chunk_size):
        chunk = text[i:i + chunk_size]
        if len(chunk) == chunk_size:
            chunks.append(chunk)

    for i in range(overlap_size, length, chunk_size):
        chunk = text[i:i + chunk_size]
        if len(chunk) == chunk_size:
            chunks.append(chunk)

    return chunks






def simpsons_chunks_opt(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        content = file.read()
    #print(content)
    chunks = content.split('\n')
    return chunks

def embed(MODEL, chunks, collection):
    for i, d in enumerate(chunks):
        response = ollama.embeddings(model=MODEL, prompt=d)
        embedding = response["embedding"]
        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[d]
        )




client = chromadb.PersistentClient(path="./db")
collection = client.create_collection(name="docs")

#chunks = create_chunks(file_path, CHUNK_SIZE, OVERLAP_SIZE)

#chunks = cofounder_match_chunks(file_path)
#chunks = chunks[:-1] # cofounder hack

#chunks = simpsons_chunks(file_path)
chunks = simpsons_chunks_opt(file_path)
#chunks = chunks[1:] # simpsons

print(f"length of chunks: {len(chunks)}")
print(f"first chunk: {chunks[0]}")

# for i in range(len(chunks)):
#     print("\n\n NEW CHUNK \n\n")
#     print(f"chunk {i}: {chunks[i]}")
# print(chunks)

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