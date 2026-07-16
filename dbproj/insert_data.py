import sqlite3

conn = sqlite3.connect('you.db')

name=input("Enter name: ")
attendance=float(input("Enter attendance: "))
marks=float(input("Enter marks: "))
result=input("Enter result: ")

cursor = conn.cursor()

cursor.execute("""  
INSERT INTO you (name, attendance, marks, result) VALUES (?, ?, ?, ?)
""", (name, attendance, marks, result))

conn.commit()
print("Data inserted successfully")

conn.close()