import flask
from flask import request, render_template, Flask

app = Flask(__name__)


@app.route('/patient_entry_form', methods=['GET', 'POST'])
def patient_entry_form():
    return render_template('patient_entry_form.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)