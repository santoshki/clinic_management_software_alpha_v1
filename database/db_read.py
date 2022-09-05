import sqlite3


def fetch_all_data():
    try:
        conn = sqlite3.connect('patient_entry_data.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT * from patient_entry_data""")
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
    fetch_data_health_issue("headache")
