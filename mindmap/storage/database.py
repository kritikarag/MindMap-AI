import json
from datetime import datetime

from mindmap.memory.embeddings import create_embedding
from mindmap.storage.connection import get_connection

def create_tables():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS journal_entries (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        journal_text TEXT NOT NULL,

        emotion TEXT,

        confidence REAL,

        observations TEXT,

        possible_patterns TEXT,

        reflection TEXT,

        created_at TEXT,
        
        embedding TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_entry(
        journal_text,
        emotion_analysis,
        reflection_analysis,
):
    embedding = json.dumps(create_embedding(journal_text))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO journal_entries
        (
        journal_text,
        emotion,
        confidence,
        observations,
        possible_patterns,
        reflection,
        created_at,
        embedding
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,

        (
            journal_text,

            emotion_analysis.dominant_emotion,

            emotion_analysis.confidence,

            str(reflection_analysis.observations),

            str(reflection_analysis.possible_patterns),

            reflection_analysis.reflection,

            datetime.now().isoformat(),

            embedding
        )
    )

    conn.commit()
    conn.close()