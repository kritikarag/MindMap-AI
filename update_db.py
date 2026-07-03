import sqlite3


conn = sqlite3.connect("mindmap.db")

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