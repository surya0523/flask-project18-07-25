from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory reminder storage
reminders = []

@app.route('/')
def home():
    return redirect(url_for('list_reminders'))

@app.route('/add', methods=['GET', 'POST'])
def add_reminder():
    if request.method == 'POST':
        title = request.form['title']
        reminder_id = len(reminders) + 1
        reminders.append({'id': reminder_id, 'title': title})
        return redirect(url_for('list_reminders'))
    return render_template('add_reminder.html')

@app.route('/reminders')
def list_reminders():
    return render_template('reminders.html', reminders=reminders)

@app.route('/delete/<int:reminder_id>')
def delete_reminder(reminder_id):
    global reminders
    reminders = [r for r in reminders if r['id'] != reminder_id]
    return redirect(url_for('list_reminders'))

if __name__ == '__main__':
    app.run(debug=True)
