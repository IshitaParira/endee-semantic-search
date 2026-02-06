from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    """
    Converts text into embedding vector
    """
    return model.encode(text).tolist()
