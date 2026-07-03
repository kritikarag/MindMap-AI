from sentence_transformers import SentenceTransformer
import json
import sqlite3
import numpy as np

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def create_embedding(text):
    vectors = model.encode(text)
    return vectors.tolist()

def similarity(a,b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))

def find_similar_entries(query):
    query_embedding = create_embedding(query)

    conn = sqlite3.connect("mindmap.db")

    cursor = conn.cursor()

    cursor.execute("""SELECT journal_text, embedding FROM journal_entries""")

    results = []

    for text, embedding in cursor.fetchall():
        if embedding is None:
            continue
        score = similarity(query_embedding, json.loads(embedding))
        results.append([score, text])

    results.sort(reverse=True)

    return results[:3]

print(
 find_similar_entries(
   "I feel tired from work"
 )
)