from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('./index.html')


@app.route("/<string:page_name>")
def works(page_name=None):
    return render_template(page_name)


def write_to_file(data_p):
    with open('database.txt', mode='a') as database:
        email = data_p['email']
        sub = data_p['subject']
        message = data_p['message']
        database.write(f'\n{email}, {sub}, {message}')


def write_to_csv(data_p):
    with open('database2.csv', mode='a', newline='') as database2:
        email = data_p['email']
        sub = data_p['subject']
        message = data_p['message']
        csv_writer = csv.writer(database2, delimiter=',')
        csv_writer.writerow([email, sub, message])


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'did no save.'
    else:
        return 'Something went wrong.Try again!!'
