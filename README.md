# Semantic Search System using Endee Vector Database

## Project Overview

This project demonstrates a **Semantic Search System** built using **Endee (nD)** as the vector database.

The system stores document embeddings in Endee and performs similarity-based retrieval using vector search.

Instead of keyword matching, the system retrieves documents based on semantic meaning.

---

## Objective

To build a practical AI/ML application using:

- Vector embeddings
- Endee as the vector database
- Similarity search for document retrieval

This project fulfills the requirement of demonstrating a real-world use case where **vector search is core**.

---

## How It Works

1. Documents are loaded from a text file.
2. Each document is converted into an embedding using `sentence-transformers`.
3. The embeddings are stored in Endee.
4. When a user enters a query:
   - The query is converted into an embedding.
   - Endee performs similarity search.
   - Top matching documents are returned.

---

## Architecture

User Query
↓
Convert to Embedding
↓
Search in Endee Vector Database
↓
Retrieve Top Similar Documents
↓
Display Results


---

## Tech Stack

- Python
- Endee (Open Source Vector Database)
- Sentence-Transformers
- Docker (for running Endee)
- REST API integration

---
