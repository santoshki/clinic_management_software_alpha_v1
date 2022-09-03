import sqlite3
import pathlib

current_dir = pathlib.Path(__file__).parent


def db_insert(patient_data):
    print("Patient data received.\n", patient_data)
    db_name = "patient_entry_data.db"
    db_path = str(current_dir)
    conn = sqlite3.connect(db_path + "\\" + db_name)
    cursor = conn.cursor()
    try:
        cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='patient_entry_data' ''')
        if cursor.fetchone()[0] == 0:
            table_create = """CREATE TABLE patient_entry_data(FIRSTNAME TEXT, MIDDLENAME TEXT, LASTNAME TEXT, EMERGENCYCONTACTNAME TEXT,
                            EMERGENCYCONTACTNUMBER TEXT, EMERGENCYCONTACTEMAILID TEXT)"""
            cursor.execute(table_create)
            conn.commit()
            print("Table created in SQLlite DB.")

        cursor.execute("INSERT INTO patient_entry_data(FIRSTNAME, MIDDLENAME, LASTNAME, EMERGENCYCONTACTNAME, EMERGENCYCONTACTNUMBER, EMERGENCYCONTACTEMAILID) VALUES (?,?,?,?,?,?)",
                       (patient_data[0], patient_data[1], patient_data[2], patient_data[3], patient_data[4], patient_data[5]))
        conn.commit()
        print("Data inserted in SQL lite db")
        return 1
    except Exception as e:
        print("Exception occurred:", e)
        return 0
