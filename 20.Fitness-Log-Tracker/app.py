from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory workout log list
logs = []

@app.route('/')
def home():
    return redirect(url_for('logs_page'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        log_id = len(logs) + 1
        workout = {
            'id': log_id,
            'type': request.form['type'],
            'duration': request.form['duration'],
            'notes': request.form['notes'],
            'date': request.form['date'],
            'icon': 'run.png' if request.form['type'].lower() == 'running' else 'lift.png'
        }
        logs.append(workout)
        return redirect(url_for('logs_page'))
    return render_template('add.html')

@app.route('/logs')
def logs_page():
    filter_date = request.args.get('date')
    if filter_date:
        filtered = [log for log in logs if log['date'] == filter_date]
    else:
        filtered = logs
    return render_template('logs.html', logs=filtered, filter_date=filter_date)

@app.route('/log/<int:log_id>')
def log_detail(log_id):
    log = next((l for l in logs if l['id'] == log_id), None)
    if not log:
        return "Log not found", 404
    return render_template('log.html', log=log)
if __name__ == '__main__':
    app.run(debug=True)