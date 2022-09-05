from flask import render_template, Flask, request
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
        patient_entry_form_data = []

        try:
            form_data = request.form
            patient_entry_form_data = entity_parser.entry_data_parser(form_data)
            db_entity.db_insert_entry_data(patient_entry_form_data)
            return "Patient data recorded successfully."
        except Exception as e:
            print("Exception occurred:", e)
            return "Exception occurred."


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
