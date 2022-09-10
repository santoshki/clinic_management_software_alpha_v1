from flask import render_template, Flask, request, flash
from database import db_entity
from data_parser import entity_parser

app = Flask(__name__)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login_form.html')


@app.route('/patient_entry_form/', methods=['GET', 'POST'])
def patient_entry_form():
    return render_template('patient_entry_form.html')


@app.route('/patient_vitals_data/', methods=['GET', 'POST'])
def patient_vitals_data():

    return render_template('patient_vitals_form.html')


@app.route('/patient_data_recorded/', methods=['GET', 'POST'])
def patient_data_recorded():
    if request.method == "POST":
        try:

            entry_form_data = request.form
            patient_entry_form_data = entity_parser.entry_data_parser(entry_form_data)
            db_entity.db_insert_entry_data(patient_entry_form_data)
            return "Patient data recorded successfully."
        except Exception as e:
            print("Exception occurred:", e)
            return "Exception occurred."


@app.route('/patient_vitals_recorded', methods=['GET', 'POST'])
def patient_vitals_recorded():
    if request.method == "POST":
        try:
            save_submit_button_pressed = request.form.get("save_submit_button")
            back_button_pressed = request.form.get("back_button")
            skip_button_pressed = request.form.get("skip_button")
            reset_button_pressed = request.form.get("reset_form_data_button")
            if save_submit_button_pressed is not None:
                print("Save and submit button pressed.")
                print("Capturing patient vitals data")
                vitals_form_data = request.form
                patient_vitals_form_data = entity_parser.patient_vitals_data_parser(vitals_form_data)
                db_entity.db_insert_vitals(patient_vitals_form_data)
                print("Patient vitals data recorded successfully.")
                return "Patient vitals data recorded successfully."
            elif back_button_pressed is not None:
                print("Back button pressed.")
                print("Reloading patient entry form...")
                return render_template('patient_entry_form.html')
            elif skip_button_pressed is not None:
                print("Skip button pressed.")
                print("Patient vitals data not recorded")
                return "Patient vitals data skipped"
            elif reset_button_pressed is not None:
                print("Reset button pressed.")
                print("Resetting form values")
                return render_template('patient_vitals_form.html')
        except Exception as e:
            print("Exception occurred:", e)
            return "Exception occurred."


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
