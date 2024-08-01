from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import ollama
import sys
import time
import random
import sys
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv('../.env')
OPENAI_KEY = os.getenv('OPENAI_KEY')
client = OpenAI(api_key=OPENAI_KEY)
'''
init stuff (strings set four coords and dart is the throw)

'''
MODEL = 'snowflake-arctic-embed:latest'

def random_square(max_x, min_x, max_y, min_y, size):
    # Ensure the rectangle is large enough to contain a 2x2 square
    if max_x - min_x < 2 or max_y - min_y < size:
        return None
    
    # Generate random top-left corner of the 2x2 square
    x = random.uniform(min_x, max_x - size)
    y = random.uniform(min_y, max_y - size)
    

    
    return x, y

        
#strings = ['really tasty delicious', 'disgusting awful overcooked', 'intriguing and interesting taste profile', 'decent but not memorable']
#strings = ['lawful', 'chaotic', 'good', 'evil']
strings = ['low', 'high', 'cold', 'hot']
strings = ['quick', 'slow', 'cold', 'hot']
dart = 'sun'


'''
GAMEPLAY
'''

vectors = []
for string in strings:
    vectors.append(ollama.embeddings(model=MODEL, prompt=string)['embedding'])

pca = PCA(n_components=2)
vectors_2d = pca.fit_transform(vectors)
max_x = int(max(vectors_2d[:, 0])) + 1
min_x = int(min(vectors_2d[:, 0])) -1
max_y = int(max(vectors_2d[:, 1])) + 1
min_y = int(min(vectors_2d[:, 1])) - 1

rect_size = min((max_x - min_x), (max_y - min_y)) - 1

x, y = random_square(max_x, min_x, max_y, min_y, rect_size)


dart_vec = ollama.embeddings(model=MODEL, prompt=dart)['embedding']
dart_2d = pca.transform([dart_vec])
dart_2d = dart_2d[0]



while True:

    while True:
        plt.figure(figsize=(10, 10))
        plt.scatter(vectors_2d[:, 0], vectors_2d[:, 1], c='blue')
        for i, txt in enumerate(strings):
            plt.annotate(txt, (vectors_2d[i, 0], vectors_2d[i, 1]))    
        plt.annotate(dart, (dart_2d[0], dart_2d[1]), c='red')
        rect = patches.Rectangle((x, y), rect_size, rect_size, linewidth=1, edgecolor='r', facecolor='none')
        
        # Add the rectangle to the plot
        plt.gca().add_patch(rect)    
        plt.show()
        dart = input('Enter a word: ')
        dart_vec = ollama.embeddings(model=MODEL, prompt=dart)['embedding']
        dart_2d = pca.transform([dart_vec])
        dart_2d = dart_2d[0]
        
        # check for hit 
        if (dart_2d[0] >= x) and (dart_2d[0] <= x + rect_size) and (dart_2d[1] >= y) and (dart_2d[1] <= y + rect_size):
            print("Hit!")
            break
        else:
            print("Miss!")
    
    rect_size = 4 * rect_size // 5
    

