from flask import Flask, render_template, request, redirect, url_for
from slots import slots

app = Flask(__name__)

@app.route('/')
def home():
    date_filter = request.args.get('date')
    filtered = [s for s in slots if s["date"] == date_filter] if date_filter else slots
    return render_template("home.html", slots=filtered)

@app.route('/book/<int:id>', methods=['GET', 'POST'])
def book(id):
    slot = next((s for s in slots if s["id"] == id), None)
    if request.method == 'POST':
        name = request.form['name']
        vehicle = request.form['vehicle']
        slot["available"] = False
        return redirect(url_for('confirm', name=name, location=slot["location"]))
    return render_template("book.html", slot=slot)

@app.route('/confirm')
def confirm():
    name = request.args.get('name')
    location = request.args.get('location')
    return render_template("confirm.html", name=name, location=location)

if __name__ == '__main__':
    app.run(debug=True)
