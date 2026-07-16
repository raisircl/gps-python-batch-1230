import sqlite3

conn = sqlite3.connect('you.db')

sid=int(input("Enter the id of the record you want to update: "))

cursor = conn.cursor()

cursor.execute("""
delete from you where id=?
""", (sid,))

conn.commit()
print("Data deleted successfully")

conn.close()