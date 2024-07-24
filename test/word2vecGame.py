from gensim.models import KeyedVectors
from scipy.spatial.distance import cosine

word_vectors = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)


def cosine_similarity(vec1, vec2):
    return 1 - cosine(vec1, vec2)

print("Hello")
# Get vector for a word
target = 'Warsaw'
target_vec = word_vectors[target]
print(len(target_vec))

user_input = "Paris"
input_vec = word_vectors[user_input]

# while True:
#     user_input = input("Enter a word: ")
#     try:
#         input_vec = word_vectors[user_input]
#         break  # Exit the inner loop if the word is found
#     except KeyError:
#         print(f"'{user_input}' not found in vocabulary. Please try another word.")


while True:
    print("THE INPUT WORD IS: (start of loop) ", user_input)
    print("EDIT IT BY ADDING...")
    while True:
        
        user_input_alter = input("Enter a word to add: ")
        try:
            input_vec_alter = word_vectors[user_input_alter]
            break  # Exit the inner loop if the word is found
        except KeyError:
            print(f"'{user_input_alter}' not found in vocabulary. Please try another word.")
        
    new_vec = input_vec + input_vec_alter   
    #print(len(input_vec))
    
    # res = cosine_similarity(target_vec, new_vec)
    # print(f"res is {res}")
    # print(f"word is : {user_input}")
    # print(f"target is : {target}")
    
    similar_words = word_vectors.most_similar(new_vec)
    #print(similar_words)
        # Extract just the words (without similarity scores) and remove the first one
    similar_word_list = [word for word, _ in similar_words[1:]]
    similar_original = similar_word_list.copy()

    # Create variations and add them to the list
    variations = []
    for word in similar_word_list:
        variations.extend([
            word.lower(),
            word.upper(),
            word.capitalize(),
            word.title()
        ])

    # Combine original words and variations, and remove duplicates
    similar_word_list = list(set(similar_word_list + variations))
    

    # Now check if the target is in the expanded list
    if target.lower() in [word.lower() for word in similar_word_list]:
        print("OMG YOU WIN!!!!")
    
    # Print the list of similar words with indices
    for i, word in enumerate(similar_original):
        print(f"{i}: {word}")
    
    user_input = similar_original[0] if user_input != similar_original[0] else similar_original[1]
    input_vec = word_vectors[user_input]
    print("USER INPUT IS NOWWWW...(end of the loop)", user_input)
    
    
    # input_vec = ....
    # user_input = ...
    # king_vec = word_vectors['king']

    # man_vec = word_vectors['man']

    # vector3 = king_vec - man_vec

    # #print(vector)
    # # Find similar words
    # similar_words = word_vectors.most_similar(vector3)
    # print(similar_words)
    
    
'''
TARGET:
Start: 
(right now am letting user pick start, I think that confuses things.)


LOOP:


    User chooses word. 

    Word is turned to vector, added to vector for Start. This is New_vector. 
    Words similar to New_Vector are found. 
    
    CHECK FOR WIN: is TARGET in words similar?
        IF yes, BREAK, you win. 
        IF no, continue. Incriment count maybe???
    
    Start -> similar_words[1] (or first similar word that isn't the word itself?)




'''