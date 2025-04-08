from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)
CSV_FILE = 'appointments.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'gender': request.form['gender'],
        'date': request.form['date'],
        'time': request.form['time'],
        'reason': request.form['reason']
    }

    # Write to CSV
    write_headers = not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if write_headers:
            writer.writeheader()
        writer.writerow(data)

    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)