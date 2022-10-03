from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/<newpage>")
def new_page(newpage):
    return render_template(f'{newpage}.html')

def save_data(data):
    with open('database.txt', mode='a') as database:
        name = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n {name}, {subject}, {message}')

def save_data_csv(data):
    with open('database.csv', mode='a') as database2:

        name = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_data_csv(data)
        return render_template('submitted.html')
    else:
        return 'error'
