from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory subscriber storage
subscribers = []

@app.route('/')
def home():
    return redirect(url_for('signup'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        signup_date = datetime.now().date()
        subscribers.append({"name": name, "email": email, "date": signup_date})
        return redirect(url_for('thankyou'))
    return render_template('signup.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/subscribers')
def list_subscribers():
    date_filter = request.args.get('date')  # expects 'YYYY-MM-DD'
    filtered = subscribers
    if date_filter:
        try:
            filter_date = datetime.strptime(date_filter, '%Y-%m-%d').date()
            filtered = [s for s in subscribers if s['date'] == filter_date]
        except ValueError:
            filtered = []  # invalid date format shows no results
    return render_template('subscribers.html', subscribers=filtered, date_filter=date_filter)

if __name__ == '__main__':
    app.run(debug=True)
