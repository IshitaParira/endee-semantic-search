from app.embed import get_embedding
from app.endee_client import create_index, add_vector, search_vector

INDEX_NAME = "documents"

def setup_documents():
    create_index(INDEX_NAME)

    with open("data/documents.txt", "r") as f:
        docs = f.readlines()

    for i, doc in enumerate(docs):
        embedding = get_embedding(doc.strip())
        add_vector(
            INDEX_NAME,
            str(i),
            embedding,
            {"text": doc.strip()}
        )

def run_search():
    query = input("Enter your query: ")
    query_embedding = get_embedding(query)
    results = search_vector(INDEX_NAME, query_embedding)

    print("\nTop Results:")
    print(results)
