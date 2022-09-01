from flask import render_template, Flask

app = Flask(__name__)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login_form.html')


@app.route('/patient_entry_form', methods=['GET', 'POST'])
def patient_entry_form():
    return render_template('patient_entry_form.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
