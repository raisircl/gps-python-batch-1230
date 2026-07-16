import sqlite3

conn = sqlite3.connect("you.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM you")

records = cursor.fetchall()

for row in records:
    print("ID:", row[0])
    print("Name:", row[1])
    print("Attendance:", row[2])
    print("Marks:", row[3])
    print("Result:", row[4])
    print("-" * 30)

conn.close()
