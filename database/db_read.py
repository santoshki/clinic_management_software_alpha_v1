import sqlite3


def fetch_all_data(dbname):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        if dbname == "patient_entry_data.db":
            cursor.execute("""SELECT * from patient_entry_data""")
        elif dbname == "patients_vitals_data.db":
            cursor.execute("""SELECT * from patients_vitals_data""")
        result = cursor.fetchall();
        print("Data stored in db:", result)

    except Exception as e:
        print("Exception occurred:", e)


def fetch_data_health_issue(query):
    try:

        conn = sqlite3.connect('patient_entry_data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patient_entry_data WHERE HEALTHISSUE=?", (query,))
        result = cursor.fetchall()
        for row in result:
            print(row)

    except Exception as e:
        print("Exception occurred:", e)


if __name__ == '__main__':
    dbname = "patient_entry_data.db"
    fetch_all_data(dbname)
