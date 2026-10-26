from mindmap.storage.connection import get_connection

conn = get_connection()

cursor = conn.cursor()


cursor.execute(
    "SELECT * FROM journal_entries"
)


rows = cursor.fetchall()


for row in rows:
    print(row)