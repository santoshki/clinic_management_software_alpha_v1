from flask import request, render_template, Flask

app = Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def patient_entry_form():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)