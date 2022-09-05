import sqlite3
import pathlib

current_dir = pathlib.Path(__file__).parent


def db_insert_entry_data(patient_data):
    print("Patient data received.\n", patient_data)
    db_name = "patient_entry_data.db"
    db_path = str(current_dir)
    conn = sqlite3.connect(db_path + "\\" + db_name)
    cursor = conn.cursor()
    try:
        cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='patient_entry_data' ''')
        if cursor.fetchone()[0] == 0:
            table_create = """CREATE TABLE patient_entry_data(FIRSTNAME TEXT, MIDDLENAME TEXT, LASTNAME TEXT, EMERGENCYCONTACTNAME TEXT,
                            EMERGENCYCONTACTNUMBER TEXT, EMERGENCYCONTACTEMAILID TEXT, PATIENTGENDER TEXT, PATIENTAGE TEXT, HEALTHISSUE TEXT, 
                            PATIENTEMAILID TEXT, PATIENTCONTACTNUMBER TEXT, PATIENTUNIQUEIDENTIFICATIONNUMBER TEXT, PATIENTIENTCITYTOWN TEXT, 
                            PATIENTSTATE TEXT, PATIENTPOSTALADDRESS TEXT, PATIENTPINCODE TEXT, DOCTORPHYSICIANNAME TEXT, PATIENTVISITNUMBER TEXT,
                            PATIENTVISITTIME TEXT)"""
            cursor.execute(table_create)
            conn.commit()
            print("Table created in SQLlite DB.")

        cursor.execute(
            "INSERT INTO patient_entry_data(FIRSTNAME, MIDDLENAME, LASTNAME, EMERGENCYCONTACTNAME, EMERGENCYCONTACTNUMBER, "
            "EMERGENCYCONTACTEMAILID,  PATIENTGENDER, PATIENTAGE, HEALTHISSUE, PATIENTEMAILID, PATIENTCONTACTNUMBER, PATIENTUNIQUEIDENTIFICATIONNUMBER,"
            "PATIENTIENTCITYTOWN, PATIENTSTATE, PATIENTPOSTALADDRESS, PATIENTPINCODE, DOCTORPHYSICIANNAME, PATIENTVISITNUMBER,"
            "PATIENTVISITTIME) "
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (patient_data[0], patient_data[1], patient_data[2], patient_data[3], patient_data[4], patient_data[5],
             patient_data[6],
             patient_data[7], patient_data[8], patient_data[9], patient_data[10], patient_data[11], patient_data[12],
             patient_data[13],
             patient_data[14], patient_data[15], patient_data[16], patient_data[17], patient_data[18]))
        conn.commit()
        print("Data inserted in SQL lite db")
        return 1
    except Exception as e:
        print("Exception occurred:", e)
        return 0


def insert_db_solution(solution_data):
    try:
        db_name = "health_issue_solution_data.db"
        db_path = str(current_dir)
        conn = sqlite3.connect(db_path + "\\" + db_name)
        cursor = conn.cursor()
        try:
            cursor.execute(
                ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='health_issue_solution_data' ''')
            if cursor.fetchone()[0] == 0:
                table_create = """CREATE TABLE health_issue_solution_data(HEALTHISSUE TEXT, DIAGNOSISTYPE TEXT, MEDICINE TEXT, 
                                PHYSICALEXCERCISE TEXT)"""
                cursor.execute(table_create)
                conn.commit()
                print("Table created in SQLlite DB.")

            cursor.execute("INSERT INTO health_issue_solution_data(HEALTHISSUE, DIAGNOSISTYPE, MEDICINE, "
                           "PHYSICALEXCERCISE) "
                           "VALUES (?,?,?,?)",
                           (solution_data[0], solution_data[1], solution_data[2], solution_data[3]))
            conn.commit()
            print("Data inserted in SQL lite db")
        except Exception as e:
            print("Exception occurred:", e)
    except Exception as e:
        print("Exception occurred:", e)
