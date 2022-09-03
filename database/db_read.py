import sqlite3

conn = sqlite3.connect('patient_entry_data.db')

cursor = conn.cursor()
cursor.execute("""SELECT * from patient_entry_data""")

result = cursor.fetchall();
print("Data stored in db:", result)