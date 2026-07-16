import sqlite3

conn = sqlite3.connect('you.db')
sid=int(input("Enter the id of the record you want to update: "))

name=input("Enter name: ")
attendance=float(input("Enter attendance: "))
marks=float(input("Enter marks: "))
result=input("Enter result: ")

cursor = conn.cursor()

cursor.execute("""  
UPDATE you SET name=?, attendance=?, marks=?, result=? WHERE id=?
""", (name, attendance, marks, result, sid))

conn.commit()
print("Data updated successfully")

conn.close()