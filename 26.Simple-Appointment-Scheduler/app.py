from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

appointments = []

@app.route('/')
def home():
    return redirect(url_for('list_appointments'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_appointment = {
            'id': len(appointments) + 1,
            'name': request.form['name'],
            'date': request.form['date'],
            'time': request.form['time'],
            'notes': request.form['notes']
        }
        appointments.append(new_appointment)
        return redirect(url_for('list_appointments'))
    return render_template('add.html')

@app.route('/appointments')
def list_appointments():
    filter_date = request.args.get('date')
    if filter_date:
        filtered = [a for a in appointments if a['date'] == filter_date]
    else:
        filtered = appointments
    return render_template('list.html', appointments=filtered, filter_date=filter_date)

@app.route('/appointment/<int:appointment_id>')
def detail(appointment_id):
    appt = next((a for a in appointments if a['id'] == appointment_id), None)
    if not appt:
        return "Appointment not found", 404
    return render_template('detail.html', appointment=appt)

if __name__ == '__main__':
    app.run(debug=True)
