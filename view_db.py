import sqlite3

conn = sqlite3.connect("mindmap.db")

cursor = conn.cursor()


cursor.execute(
    "SELECT * FROM journal_entries"
)


rows = cursor.fetchall()


for row in rows:
    print(row)