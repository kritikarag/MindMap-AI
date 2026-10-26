from mindmap.storage.connection import get_connection


conn = get_connection()

cursor = conn.cursor()


cursor.execute(
    """
    ALTER TABLE journal_entries
    ADD COLUMN embedding TEXT
    """
)


conn.commit()
conn.close()

print("Database updated")