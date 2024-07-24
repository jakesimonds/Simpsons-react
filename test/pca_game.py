from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import ollama
import sys
import time
'''
init stuff (strings set four coords and dart is the throw)

'''
MODEL = 'snowflake-arctic-embed:latest'

        
#strings = ['really tasty delicious', 'disgusting awful overcooked', 'intriguing and interesting taste profile', 'decent but not memorable']
strings = ['low', 'cold', 'high', 'hot']

dart = 'sun'


'''
GAMEPLAY
'''

vectors = []
for string in strings:
    vectors.append(ollama.embeddings(model=MODEL, prompt=string)['embedding'])

pca = PCA(n_components=2)
vectors_2d = pca.fit_transform(vectors)
dart_vec = ollama.embeddings(model=MODEL, prompt=dart)['embedding']
dart_2d = pca.transform([dart_vec])





while True:
    plt.figure(figsize=(10, 10))
    plt.scatter(vectors_2d[:, 0], vectors_2d[:, 1], c='blue')
    for i, txt in enumerate(strings):
        plt.annotate(txt, (vectors_2d[i, 0], vectors_2d[i, 1]))    
    plt.annotate(dart, (dart_2d[0, 0], dart_2d[0, 1]), c='red')    
    plt.show()
    dart = input('Enter a word: ')
    dart_vec = ollama.embeddings(model=MODEL, prompt=dart)['embedding']
    dart_2d = pca.transform([dart_vec])
    

