from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store guestbook entries
entries = []

@app.route('/')
def index():
    return render_template("index.html", entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    name = request.form['name']
    message = request.form['message']
    avatar = url_for('static', filename='avatars/default.png')  # static avatar
    entry_id = len(entries) + 1
    entries.append({'id': entry_id, 'name': name, 'message': message, 'avatar': avatar})
    return redirect(url_for('index'))

@app.route('/entry/<int:entry_id>')
def view_entry(entry_id):
    entry = next((e for e in entries if e['id'] == entry_id), None)
    if entry:
        return render_template('entry.html', entry=entry)
    return "Entry not found", 404

if __name__ == '__main__':
    app.run(debug=True)
