import requests

BASE_URL = "http://localhost:8080"

def create_index(index_name):
    url = f"{BASE_URL}/api/v1/index/create"
    payload = {
        "index_name": index_name,
        "dimension": 384
    }
    requests.post(url, json=payload)

def add_vector(index_name, vector_id, vector, metadata):
    url = f"{BASE_URL}/api/v1/vector/add"
    payload = {
        "index_name": index_name,
        "vectors": [
            {
                "id": vector_id,
                "values": vector,
                "metadata": metadata
            }
        ]
    }
    requests.post(url, json=payload)

def search_vector(index_name, query_vector, top_k=2):
    url = f"{BASE_URL}/api/v1/vector/search"
    payload = {
        "index_name": index_name,
        "query_vector": query_vector,
        "top_k": top_k
    }
    response = requests.post(url, json=payload)
    return response.json()
