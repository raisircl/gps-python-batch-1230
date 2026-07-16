import sqlite3

#establish the connectio with db file
conn = sqlite3.connect('you.db')

# create a cursor object for CRUD Operationd
cursor = conn.cursor()

print("Database connected successfully")

cursor.execute("""
CREATE TABLE IF NOT EXISTS you (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    attendance REAL,
    marks REAL,
    result TEXT
)
""")

conn.commit()
conn.close()

print("Table created successfully")

