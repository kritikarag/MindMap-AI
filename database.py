import sqlite3
from datetime import datetime

DB_NAME = "mindmap.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

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

        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_entry(
        journal_text,
        emotion_analysis,
        reflection_analysis,
):
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
        created_at
        )

        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,

        (
            journal_text,

            emotion_analysis.dominant_emotion,

            emotion_analysis.confidence,

            str(reflection_analysis.observations),

            str(reflection_analysis.possible_patterns),

            reflection_analysis.reflection,

            datetime.now().isoformat()
        )
    )

    conn.commit()
    conn.close()