from flask import Flask, render_template, request, redirect, url_for
from events import events

app = Flask(__name__)

@app.route('/')
def home():
    registered = request.args.get('registered')
    return render_template("home.html", events=events, registered=registered)

@app.route('/event/<int:event_id>')
def event_detail(event_id):
    event = next((e for e in events if e["id"] == event_id), None)
    return render_template("event_detail.html", event=event)

@app.route('/register/<int:event_id>', methods=['POST'])
def register(event_id):
    name = request.form['name']
    email = request.form['email']
    # You can save registration data or send email here
    return redirect(url_for('home', registered='yes'))

if __name__ == '__main__':
    app.run(debug=True)
