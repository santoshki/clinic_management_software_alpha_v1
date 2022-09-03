from flask import render_template, Flask, request
from database import db_entity

app = Flask(__name__)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login_form.html')


@app.route('/patient_entry_form', methods=['GET', 'POST'])
def patient_entry_form():
    return render_template('patient_entry_form.html')


@app.route('/patient_data_recorded', methods=['GET', 'POST'])
def patient_data_recorded():
    if request.method == "POST":
        patient_entry_form_data = []
        try:
            form_data = request.form
            patient_firstname = form_data["first_name"]
            patient_middlename = form_data["middle_name"]
            patient_lastname = form_data["last_name"]
            patient_emergency_contact_name = form_data["emergency_name"]
            patient_emergency_contact_number = form_data["emg_contact_num"]
            patient_emergency_email_id = form_data["Emergency_Email_id"]
            patient_entry_form_data.extend((patient_firstname, patient_middlename, patient_lastname,
                                            patient_emergency_contact_name, patient_emergency_contact_number,
                                            patient_emergency_email_id))
            db_entity.db_insert(patient_entry_form_data)
            return "Patient data recorded successfully."
        except Exception as e:
            print("Exception occurred:", e)
            return "Exception occurred."


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
