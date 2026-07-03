import sqlite3
from memory import create_embedding
import json


conn = sqlite3.connect("mindmap.db")

cursor = conn.cursor()


cursor.execute(
    """
    SELECT id, journal_text
    FROM journal_entries
    WHERE embedding IS NULL
    """
)


entries = cursor.fetchall()


for entry_id, text in entries:

    embedding = create_embedding(text)


    cursor.execute(
        """
        UPDATE journal_entries
        SET embedding = ?
        WHERE id = ?
        """,
        (
            json.dumps(embedding),
            entry_id
        )
    )


conn.commit()
conn.close()


print("Embeddings generated")