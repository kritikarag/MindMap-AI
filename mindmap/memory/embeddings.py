from sentence_transformers import SentenceTransformer
import json
import numpy as np

from mindmap.config import EMBEDDING_MODEL
from mindmap.storage.connection import get_connection

model = SentenceTransformer(EMBEDDING_MODEL)

def create_embedding(text):
    vectors = model.encode(text)
    return vectors.tolist()

def similarity(a,b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))

def find_similar_entries(query):
    query_embedding = create_embedding(query)

    conn = get_connection()

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
