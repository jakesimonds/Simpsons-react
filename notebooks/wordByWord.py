# import ollama
# import matplotlib.pyplot as plt
# from sklearn.decomposition import PCA

# def generate_embeddings(text):
#     words = text.split()
#     embeddings = []
#     substrings = []
    
#     for i in range(1, len(words) + 1):
#         subset = ' '.join(words[:i])
#         substrings.append(subset)
#         response = ollama.embeddings(model='snowflake-arctic-embed', prompt=subset)
#         embeddings.append(response['embedding'])
    
#     return embeddings, substrings

# def plot_embeddings(embeddings, substrings):
#     # Use PCA to reduce dimensionality to 2D for visualization
#     pca = PCA(n_components=2)
#     reduced_embeddings = pca.fit_transform(embeddings)
    
#     plt.figure(figsize=(12, 8))
#     plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1])
    
#     for (x, y), label in zip(reduced_embeddings, substrings):
#         plt.annotate(label, (x, y), xytext=(5, 5), textcoords='offset points', fontsize=8, 
#                      bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.7))
    
#     plt.title('Embedding Progression')
#     plt.xlabel('PCA Component 1')
#     plt.ylabel('PCA Component 2')
#     plt.tight_layout()
#     plt.show()

# # Example usage
# #text = "You are amazing. Amazingly bad. I'm amazingly badly in love with you and your terribleness"
# #text = 'He loves me. He loves me not. He loves me. He loves me not.'
# text = 'So many little words, so many little phrases, love though is important. Brotherly love. '
# embeddings, substrings = generate_embeddings(text)
# plot_embeddings(embeddings, substrings)

import ollama
import matplotlib.pyplot as plt
import numpy as np

def generate_embeddings(text):
    words = text.split()
    embeddings = []
    substrings = []
    
    for i in range(1, len(words) + 1):
        subset = ' '.join(words[:i])
        substrings.append(subset)
        response = ollama.embeddings(model='snowflake-arctic-embed', prompt=subset)
        embeddings.append(response['embedding'])
    
    return embeddings, substrings

def plot_all_embeddings(embeddings, substrings):
    n_embeddings = len(embeddings)
    fig, axes = plt.subplots(n_embeddings, 1, figsize=(20, 4*n_embeddings), sharex=True)
    fig.suptitle('Raw Embedding Vectors for Progressive Substrings', fontsize=16)
    
    for i, (embedding, substring, ax) in enumerate(zip(embeddings, substrings, axes)):
        ax.plot(embedding, 'b-', alpha=0.7)
        ax.set_title(f'"{substring}"', fontsize=10)
        ax.set_ylabel('Value')
        ax.grid(True, alpha=0.3)
        
        # Add some statistics to each subplot
        stats = f'Min: {min(embedding):.2f}, Max: {max(embedding):.2f}, Mean: {np.mean(embedding):.2f}'
        ax.text(0.98, 0.98, stats, transform=ax.transAxes, ha='right', va='top', fontsize=8, 
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    axes[-1].set_xlabel('Embedding Dimension')
    plt.tight_layout()
    plt.show()

# Example usage
text = "The quick brown fox jumps over the lazy dog"
embeddings, substrings = generate_embeddings(text)
plot_all_embeddings(embeddings, substrings)