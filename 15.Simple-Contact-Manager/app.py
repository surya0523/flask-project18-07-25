from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory contact list
contacts = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "city": "New York"},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "city": "Los Angeles"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "city": "New York"}
]

@app.route('/')
def index():
    city_filter = request.args.get('city')
    if city_filter:
        filtered = [c for c in contacts if c['city'].lower() == city_filter.lower()]
    else:
        filtered = contacts
    return render_template('index.html', contacts=filtered, city_filter=city_filter)

@app.route('/contact/<int:contact_id>')
def contact_detail(contact_id):
    contact = next((c for c in contacts if c['id'] == contact_id), None)
    if not contact:
        return "Contact not found", 404
    return render_template('contact.html', contact=contact)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        new_id = max([c['id'] for c in contacts]) + 1 if contacts else 1
        name = request.form['name']
        email = request.form['email']
        city = request.form['city']
        contacts.append({"id": new_id, "name": name, "email": email, "city": city})
        return redirect(url_for('index'))
    return render_template('add_contact.html')

if __name__ == '__main__':
    app.run(debug=True)
